# ============================================================================
# Hugo Article Import & Processing Pipeline - Fixed Version
# ============================================================================
# Description: Automated pipeline for importing articles from Obsidian to Hugo
# Author: Fixed Script
# Date: 2026-02-10
# ============================================================================

# Set encoding to UTF-8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

# Get script directory (dynamic instead of hard-coded)
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Simple mode flag - set to $true for batch-like execution
$SimpleMode = $false

# Check for simple mode parameter
if ($args -contains "-simple") {
    $SimpleMode = $true
}

# Scripts configuration
$Scripts = @(
    @{
        Name = "convert_images.py"
        Title = "Import New Articles Images"
        Description = "Import images from Obsidian Vault Attachment to Hugo static/images"
        ReportFile = "image_migration_report.txt"
        TrackingFile = "processed_images.json"
    },
    @{
        Name = "title-adder.py"
        Title = "Add Title for New Articles"
        Description = "Add Hugo front matter title based on filename"
        ReportFile = "title_adder_report.txt"
        TrackingFile = "processed_articles.json"
    },
    @{
        Name = "altimage-adder.py"
        Title = "Add ALT for Images in Articles"
        Description = "Add ALT attributes to images based on article title"
        ReportFile = "altimage_adder_report.txt"
        TrackingFile = "processed_articles.json"
    },
    @{
        Name = "images-renamer.py"
        Title = "Rename Images in /static/images/*"
        Description = "Rename all images using slugified names"
        ReportFile = "images_renamer_report.txt"
        TrackingFile = "images_rename_mapping.json"
    },
    @{
        Name = "image-article-renamer.py"
        Title = "Update Image References in Articles"
        Description = "Update image paths in markdown files with new slugified names"
        ReportFile = "image_article_renamer_report.txt"
        TrackingFile = "processed_articles.json"
    },
    @{
        Name = "toc-remover.py"
        Title = "Remove Obsidian TOC"
        Description = "Remove Obsidian Table of Contents from all articles"
        ReportFile = "toc_remover_report.txt"
        TrackingFile = "toc_removal_tracking.json"
    },
    @{
        Name = "obsidian-property-remover-enhanced.py"
        Title = "Add Enhanced Hugo Front Matter"
        Description = "Add comprehensive Hugo front matter properties to articles"
        ReportFile = "obsidian_property_remover_enhanced_report.txt"
        TrackingFile = "property-delete-tracking-enhanced.json"
    }
)

# Global statistics
$GlobalStats = @{
    StartTime = Get-Date
    TotalSteps = $Scripts.Count
    CompletedSteps = 0
    FailedSteps = 0
    Warnings = 0
    TotalProcessedFiles = 0
    StepResults = @()
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

function Write-ColorText {
    param(
        [string]$Text,
        [string]$Color = 'White'
    )
    Write-Host $Text -ForegroundColor $Color
}

function Execute-PythonScript {
    param(
        [int]$StepNumber,
        [hashtable]$ScriptInfo
    )
    
    $scriptPath = Join-Path $ScriptDir $ScriptInfo.Name
    
    # Check if script exists
    if (-not (Test-Path $scriptPath)) {
        if (-not $SimpleMode) {
            Write-ColorText "ERROR: Script not found: $($ScriptInfo.Name)" "Red"
        } else {
            Write-Host "ERROR: Script not found: $($ScriptInfo.Name)" -ForegroundColor Red
        }
        $GlobalStats.FailedSteps++
        return $false
    }
    
    # Show step header
    if (-not $SimpleMode) {
        Write-Host ""
        Write-Host "========================================" -ForegroundColor Cyan
        Write-Host "STEP $StepNumber of $($GlobalStats.TotalSteps): $($ScriptInfo.Title)" -ForegroundColor White
        Write-Host "========================================" -ForegroundColor Cyan
        Write-Host "Description: $($ScriptInfo.Description)" -ForegroundColor Gray
        Write-Host "Script: $($ScriptInfo.Name)" -ForegroundColor Gray
        Write-Host ""
        Write-Host "Executing..." -ForegroundColor Yellow
        Write-Host ""
    } else {
        # Simple batch-like output
        Write-Host "==================: Step $StepNumber :===============" -ForegroundColor Cyan
        Write-Host "===== $($ScriptInfo.Title) =====" -ForegroundColor Cyan
        Write-Host "==============================================" -ForegroundColor Cyan
    }
    
    $startTime = Get-Date
    
    try {
        # Run Python script and capture output
        if ($SimpleMode) {
            # Direct execution like batch file
            & python.exe $scriptPath
            $exitCode = $LASTEXITCODE
        } else {
            # Enhanced execution with output capture
            $output = & python.exe $scriptPath 2>&1
            $exitCode = $LASTEXITCODE
            
            # Show Python output (filtered)
            if ($output) {
                Write-Host "----------------------------------------" -ForegroundColor DarkGray
                foreach ($line in $output) {
                    $lineStr = $line.ToString()
                    if ($lineStr -match "ERROR|FAIL|WARNING|SUCCESS|COMPLETED|processed|found") {
                        Write-Host "  $lineStr" -ForegroundColor Gray
                    }
                }
                Write-Host "----------------------------------------" -ForegroundColor DarkGray
                Write-Host ""
            }
        }
        
        $endTime = Get-Date
        $duration = ($endTime - $startTime).TotalSeconds
        
        # Check exit code
        if ($exitCode -eq 0) {
            if (-not $SimpleMode) {
                Write-ColorText "SUCCESS: Completed successfully in $([math]::Round($duration, 2))s" "Green"
            } else {
                Write-Host "Step $StepNumber completed successfully." -ForegroundColor Green
            }
            
            $GlobalStats.CompletedSteps++
            $GlobalStats.StepResults += @{
                Step = $StepNumber
                Name = $ScriptInfo.Name
                Title = $ScriptInfo.Title
                Status = "Success"
                Duration = $duration
                ExitCode = $exitCode
            }
            
            return $true
        } else {
            if (-not $SimpleMode) {
                Write-ColorText "FAILED: Exit code: $exitCode" "Red"
            } else {
                Write-Host "ERROR: Step $StepNumber failed with exit code: $exitCode" -ForegroundColor Red
            }
            
            $GlobalStats.FailedSteps++
            $GlobalStats.StepResults += @{
                Step = $StepNumber
                Name = $ScriptInfo.Name
                Title = $ScriptInfo.Title
                Status = "Failed"
                Duration = $duration
                ExitCode = $exitCode
            }
            
            return $false
        }
    }
    catch {
        if (-not $SimpleMode) {
            Write-ColorText "ERROR: Exception occurred: $($_.Exception.Message)" "Red"
        } else {
            Write-Host "ERROR: Exception in Step $StepNumber : $($_.Exception.Message)" -ForegroundColor Red
        }
        
        $GlobalStats.FailedSteps++
        $GlobalStats.StepResults += @{
            Step = $StepNumber
            Name = $ScriptInfo.Name
            Title = $ScriptInfo.Title
            Status = "Error"
            Duration = 0
            ExitCode = -1
            Error = $_.Exception.Message
        }
        
        return $false
    }
    
    if (-not $SimpleMode) {
        Write-Host ""
    } else {
        Write-Host ""
        Write-Host ""
    }
}

function Generate-FinalReport {
    $reportPath = Join-Path $ScriptDir "pipeline-execution-report.txt"
    $endTime = Get-Date
    $totalDuration = ($endTime - $GlobalStats.StartTime).TotalSeconds
    
    $report = @"
================================================================================
                 HUGO ARTICLE PROCESSING PIPELINE REPORT
================================================================================

Execution Summary
-----------------
Start Time:           $($GlobalStats.StartTime.ToString("yyyy-MM-dd HH:mm:ss"))
End Time:             $($endTime.ToString("yyyy-MM-dd HH:mm:ss"))
Total Duration:       $([math]::Round($totalDuration, 2)) seconds
Total Steps:          $($GlobalStats.TotalSteps)
Completed Steps:      $($GlobalStats.CompletedSteps)
Failed Steps:         $($GlobalStats.FailedSteps)
Success Rate:         $(if($GlobalStats.TotalSteps -gt 0){[math]::Round($GlobalStats.CompletedSteps / $GlobalStats.TotalSteps * 100, 2)}else{0})%

================================================================================
                              STEP-BY-STEP RESULTS
================================================================================

"@
    
    foreach ($result in $GlobalStats.StepResults) {
        $statusIcon = if ($result.Status -eq "Success") { "OK" } elseif ($result.Status -eq "Failed") { "FAIL" } else { "ERROR" }
        $report += @"
Step $($result.Step): $($result.Title)
$("-" * 80)
Script:     $($result.Name)
Status:     $statusIcon $($result.Status)
Duration:   $([math]::Round($result.Duration, 2))s
Exit Code:  $($result.ExitCode)

"@
        
        if ($result.Error) {
            $report += "Error:      $($result.Error)`n`n"
        }
    }
    
    $report += @"
================================================================================
                                    NOTES
================================================================================

1. Import Images:
   - Images imported from Obsidian Vault Attachment
   - Destination: static/images/[category]/

2. Add Titles:
   - Titles added to Hugo front matter based on filename
   - E-numbers removed from title
   - Required for subsequent image renaming steps

3. Add ALT Attributes:
   - ALT text added to all images
   - Based on article title property

4. Rename Images:
   - Images in static/images/ renamed with slugified names
   - Format: lowercase-with-dashes.extension

5. Update Image References:
   - Image paths in markdown updated to match new names
   - All references synchronized

6. Remove TOC:
   - Obsidian Table of Contents removed
   - Hugo will generate its own TOC

7. Add Front Matter:
   - Comprehensive Hugo front matter added
   - Includes: title, slug, date, categories, tags, SEO, Open Graph, etc.

================================================================================
                                END OF REPORT
================================================================================

Report generated: $($endTime.ToString("yyyy-MM-dd HH:mm:ss"))
Report location: $reportPath

"@
    
    # Write report to file
    try {
        $report | Out-File -FilePath $reportPath -Encoding UTF8
        return $reportPath
    }
    catch {
        Write-ColorText "WARNING: Could not write report file: $($_.Exception.Message)" "Yellow"
        return $null
    }
}

# ============================================================================
# MAIN EXECUTION
# ============================================================================

# Clear screen for better visualization
if (-not $SimpleMode) {
    Clear-Host
}

# Show main header
if (-not $SimpleMode) {
    Write-Host ""
    Write-Host "################################################################################" -ForegroundColor Cyan
    Write-Host "#                                                                              #" -ForegroundColor Cyan
    Write-Host "#          HUGO ARTICLE PROCESSING PIPELINE - FIXED VERSION                    #" -ForegroundColor Cyan
    Write-Host "#                                                                              #" -ForegroundColor Cyan
    Write-Host "################################################################################" -ForegroundColor Cyan
    Write-Host ""
    Write-ColorText "Start Time: $($GlobalStats.StartTime.ToString("yyyy-MM-dd HH:mm:ss"))" "White"
    Write-ColorText "Working Directory: $ScriptDir" "White"
    Write-ColorText "Python Scripts: $($Scripts.Count)" "White"
    Write-Host ""

    # Confirm execution
    Write-Host "Press any key to start execution, or Ctrl+C to cancel..." -ForegroundColor Yellow
    try {
        $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    } catch {
        # Fallback for non-interactive environments
        Write-Host "Auto-starting in 3 seconds..."
        Start-Sleep -Seconds 3
    }
    Write-Host ""
} else {
    Write-Host "Starting Hugo Article Processing Pipeline (Simple Mode)..."
    Write-Host "Working Directory: $ScriptDir"
    Write-Host ""
}

# Execute all scripts in sequence
for ($i = 0; $i -lt $Scripts.Count; $i++) {
    $success = Execute-PythonScript -StepNumber ($i + 1) -ScriptInfo $Scripts[$i]
    
    # Optional: Ask to continue if a step fails
    if (-not $success -and -not $SimpleMode) {
        Write-Host ""
        Write-ColorText "WARNING: Step $($i + 1) failed. Continue with next step? (Y/N)" "Yellow"
        $response = Read-Host "  "
        if ($response -ne 'Y' -and $response -ne 'y') {
            Write-ColorText "Pipeline execution cancelled by user." "Red"
            break
        }
    }
    
    # Small delay between steps for readability
    if (-not $SimpleMode) {
        Start-Sleep -Milliseconds 500
    }
}

# Generate final report
Write-Host ""
Write-ColorText "Generating comprehensive report..." "White"
$reportPath = Generate-FinalReport

# Show final summary
if (-not $SimpleMode) {
    Write-Host ""
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "EXECUTION SUMMARY" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    
    $endTime = Get-Date
    $totalDuration = ($endTime - $GlobalStats.StartTime).TotalSeconds
    
    Write-Host "Pipeline Execution Completed" -ForegroundColor White
    Write-Host ""
    
    # Statistics
    Write-Host "Statistics:" -ForegroundColor Yellow
    Write-Host ""
    Write-ColorText "Total Duration: $([math]::Round($totalDuration, 2)) seconds" "White"
    Write-ColorText "Total Steps: $($GlobalStats.TotalSteps)" "White"
    Write-ColorText "Completed: $($GlobalStats.CompletedSteps)" "Green"
    
    if ($GlobalStats.FailedSteps -gt 0) {
        Write-ColorText "Failed: $($GlobalStats.FailedSteps)" "Red"
    }
    
    $successRate = if($GlobalStats.TotalSteps -gt 0){[math]::Round($GlobalStats.CompletedSteps / $GlobalStats.TotalSteps * 100, 2)}else{0}
    Write-ColorText "Success Rate: $successRate%" $(if($successRate -eq 100){'Green'}else{'Yellow'})
    
    Write-Host ""
    
    # Step results
    Write-Host "Step Results:" -ForegroundColor Yellow
    Write-Host ""
    
    foreach ($result in $GlobalStats.StepResults) {
        $statusIcon = if ($result.Status -eq "Success") { "OK" } elseif ($result.Status -eq "Failed") { "FAIL" } else { "ERROR" }
        $statusColor = if ($result.Status -eq "Success") { "Green" } elseif ($result.Status -eq "Failed") { "Red" } else { "Yellow" }
        
        Write-Host "$statusIcon Step $($result.Step): $($result.Title) ($([math]::Round($result.Duration, 2))s)" -ForegroundColor $statusColor
    }
    
    Write-Host ""
    Write-Host ""
    
    # Report file
    if ($ReportPath) {
        Write-Host "Detailed Report:" -ForegroundColor Yellow
        Write-Host ""
        Write-ColorText "Report saved to: $ReportPath" "Green"
        Write-Host ""
    }
    
    # Final status
    if ($GlobalStats.FailedSteps -eq 0) {
        Write-Host "All Steps Completed Successfully!" -ForegroundColor Green
    } else {
        Write-Host "Pipeline completed with $($GlobalStats.FailedSteps) failed step(s)" -ForegroundColor Yellow
    }
} else {
    # Simple summary like batch file
    Write-Host "==============================" -ForegroundColor Green
    Write-Host "===== Execution Finished =====" -ForegroundColor Green
    Write-Host "==============================" -ForegroundColor Green
    Write-Host ""
    Write-Host ""
    Write-Host "====================================" -ForegroundColor Yellow
    Write-Host "======== Start Reporting ============" -ForegroundColor Yellow
    Write-Host "====================================" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "1. New Articles Image Imported Successfully from Obsidian Vault Attachment"
    Write-Host ""
    Write-Host "2. Add new title for all new articles based on Hugo Front Matter syntax, title filled based on file name"
    Write-Host ""
    Write-Host "Note: Step 2 Required for step 3 and step 4 - image renaming"
    Write-Host ""
    Write-Host "3. Add ALT Value for all new imported images based on title property"
    Write-Host ""
    Write-Host "4. Rename all new imported images in static/images/category-name/*, new name based on File Name"
    Write-Host ""
    Write-Host "5. Rename all new imported images Usages in the Markdown file based on new image name from step 4"
    Write-Host ""
    Write-Host "6. Remove All Obsidian Table of Contents"
    Write-Host ""
    Write-Host "7. Add All important front matter properties to new articles"
    Write-Host ""
    Write-Host ""
    Write-Host "=====================================" -ForegroundColor Green
    Write-Host "======== Finish Reporting ============" -ForegroundColor Green
    Write-Host "=====================================" -ForegroundColor Green
    
    if ($reportPath) {
        Write-Host ""
        Write-Host "Detailed report saved to: $reportPath"
    }
}

# End
if (-not $SimpleMode) {
    Write-Host ""
    Write-Host "################################################################################" -ForegroundColor Cyan
    Write-Host ""
}