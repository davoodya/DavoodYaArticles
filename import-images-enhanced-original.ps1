# ============================================================================
# Hugo Article Import & Processing Pipeline - Enhanced Version
# ============================================================================
# Description: Automated pipeline for importing articles from Obsidian to Hugo
# Author: Enhanced Script
# Date: 2026-02-09
# ============================================================================

# Set encoding to UTF-8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

# Colors for better visualization
$Colors = @{
    Header = 'Cyan'
    Success = 'Green'
    Warning = 'Yellow'
    Error = 'Red'
    Info = 'White'
    Step = 'Magenta'
    Highlight = 'Yellow'
}

# Script paths
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
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

function Write-ColorHeader {
    param([string]$Text, [string]$Color = 'Cyan')
    $length = $Text.Length
    $border = "=" * ($length + 4)
    Write-Host ""
    Write-Host $border -ForegroundColor $Color
    Write-Host "  $Text  " -ForegroundColor $Color
    Write-Host $border -ForegroundColor $Color
    Write-Host ""
}

function Write-ColorBox {
    param(
        [string]$Text,
        [string]$Color = 'White',
        [string]$Prefix = ""
    )
    if ($Prefix) {
        Write-Host "$Prefix " -NoNewline -ForegroundColor $Color
    }
    Write-Host $Text -ForegroundColor $Color
}

function Write-StepHeader {
    param(
        [int]$StepNumber,
        [string]$Title
    )
    Write-Host ""
    Write-Host "╔═══════════════════════════════════════════════════════════════════════════╗" -ForegroundColor $Colors.Step
    Write-Host "║" -NoNewline -ForegroundColor $Colors.Step
    Write-Host " STEP $StepNumber of $($GlobalStats.TotalSteps): $Title" -NoNewline -ForegroundColor White
    $padding = 74 - " STEP $StepNumber of $($GlobalStats.TotalSteps): $Title".Length
    Write-Host (" " * $padding) -NoNewline
    Write-Host "║" -ForegroundColor $Colors.Step
    Write-Host "╚═══════════════════════════════════════════════════════════════════════════╝" -ForegroundColor $Colors.Step
    Write-Host ""
}

function Write-Progress {
    param([string]$Status, [int]$PercentComplete)
    Write-Progress -Activity "Hugo Article Processing Pipeline" -Status $Status -PercentComplete $PercentComplete
}

function Read-JsonReport {
    param([string]$FilePath)
    
    if (Test-Path $FilePath) {
        try {
            $content = Get-Content -Path $FilePath -Raw -Encoding UTF8 | ConvertFrom-Json
            return $content
        }
        catch {
            Write-ColorBox "⚠️  Warning: Could not parse JSON file: $FilePath" -Color $Colors.Warning
            return $null
        }
    }
    return $null
}

function Read-TextReport {
    param([string]$FilePath)
    
    if (Test-Path $FilePath) {
        try {
            return Get-Content -Path $FilePath -Raw -Encoding UTF8
        }
        catch {
            Write-ColorBox "⚠️  Warning: Could not read file: $FilePath" -Color $Colors.Warning
            return $null
        }
    }
    return $null
}

function Show-StepResults {
    param(
        [string]$ReportFile,
        [string]$TrackingFile,
        [string]$ScriptName
    )
    
    Write-Host "  📊 Results:" -ForegroundColor $Colors.Highlight
    Write-Host ""
    
    # Try to read tracking file for statistics
    $trackingPath = Join-Path $ScriptDir $TrackingFile
    $tracking = Read-JsonReport -FilePath $trackingPath
    
    if ($tracking) {
        # Different tracking files have different structures
        switch ($ScriptName) {
            "convert_images.py" {
                if ($tracking.processed_images) {
                    $count = $tracking.processed_images.Count
                    Write-ColorBox "     ✅ Images imported: $count" -Color $Colors.Success
                    $GlobalStats.TotalProcessedFiles += $count
                }
            }
            "title-adder.py" {
                if ($tracking.processed_files) {
                    $count = $tracking.processed_files.Count
                    Write-ColorBox "     ✅ Articles with title added: $count" -Color $Colors.Success
                    $GlobalStats.TotalProcessedFiles += $count
                }
            }
            "images-renamer.py" {
                if ($tracking.PSObject.Properties.Name -contains 'old_name') {
                    # It's a mapping object
                    $count = ($tracking.PSObject.Properties | Measure-Object).Count
                    Write-ColorBox "     ✅ Images renamed: $count" -Color $Colors.Success
                    
                    # Show some examples (first 5)
                    if ($count -gt 0 -and $count -le 5) {
                        Write-Host "     📝 Renamed images:" -ForegroundColor $Colors.Info
                        foreach ($prop in $tracking.PSObject.Properties) {
                            $oldName = $prop.Name
                            $newName = $prop.Value
                            Write-Host "        • $oldName → $newName" -ForegroundColor Gray
                        }
                    }
                    elseif ($count -gt 5) {
                        Write-Host "     📝 Sample renamed images (first 5):" -ForegroundColor $Colors.Info
                        $i = 0
                        foreach ($prop in $tracking.PSObject.Properties) {
                            if ($i -ge 5) { break }
                            $oldName = $prop.Name
                            $newName = $prop.Value
                            Write-Host "        • $oldName → $newName" -ForegroundColor Gray
                            $i++
                        }
                        Write-Host "        ... and $($count - 5) more" -ForegroundColor Gray
                    }
                }
            }
            "toc-remover.py" {
                if ($tracking.processed_files) {
                    $count = $tracking.processed_files.Count
                    Write-ColorBox "     ✅ TOC removed from: $count articles" -Color $Colors.Success
                    $GlobalStats.TotalProcessedFiles += $count
                }
            }
            "obsidian-property-remover-enhanced.py" {
                if ($tracking.processed_files) {
                    $count = $tracking.processed_files.Count
                    Write-ColorBox "     ✅ Front matter added to: $count articles" -Color $Colors.Success
                    $GlobalStats.TotalProcessedFiles += $count
                }
            }
            default {
                if ($tracking.processed_files) {
                    $count = $tracking.processed_files.Count
                    Write-ColorBox "     ✅ Files processed: $count" -Color $Colors.Success
                    $GlobalStats.TotalProcessedFiles += $count
                }
            }
        }
        
        # Show last run time if available
        if ($tracking.last_run) {
            Write-ColorBox "     🕐 Last run: $($tracking.last_run)" -Color Gray
        }
    }
    
    # Try to read text report for additional info
    $reportPath = Join-Path $ScriptDir $ReportFile
    if (Test-Path $reportPath) {
        Write-ColorBox "     📄 Detailed report: $ReportFile" -Color $Colors.Info
    }
    
    Write-Host ""
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
            Write-ColorBox "❌ Script not found: $($ScriptInfo.Name)" -Color $Colors.Error
        } else {
            Write-Host "ERROR: Script not found: $($ScriptInfo.Name)" -ForegroundColor Red
        }
        $GlobalStats.FailedSteps++
        return $false
    }
    
    # Show step header
    if (-not $SimpleMode) {
        Write-StepHeader -StepNumber $StepNumber -Title $ScriptInfo.Title
        Write-ColorBox "  📝 Description: $($ScriptInfo.Description)" -Color $Colors.Info
        Write-Host "  🐍 Script: $($ScriptInfo.Name)" -ForegroundColor Gray
        Write-Host ""
        Write-ColorBox "  ⚙️  Executing..." -Color $Colors.Info
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
                Write-Host "  " -NoNewline
                Write-Host "─" * 75 -ForegroundColor DarkGray
                foreach ($line in $output) {
                    $lineStr = $line.ToString()
                    if ($lineStr -match "ERROR|FAIL|WARNING|SUCCESS|COMPLETED|processed|found") {
                        Write-Host "  $lineStr" -ForegroundColor Gray
                    }
                }
                Write-Host "  " -NoNewline
                Write-Host "─" * 75 -ForegroundColor DarkGray
                Write-Host ""
            }
        }
        
        $endTime = Get-Date
        $duration = ($endTime - $startTime).TotalSeconds
        
        # Check exit code
        if ($exitCode -eq 0) {
            if (-not $SimpleMode) {
                Write-ColorBox "  ✅ Completed successfully in $([math]::Round($duration, 2))s" -Color $Colors.Success
                Show-StepResults -ReportFile $ScriptInfo.ReportFile -TrackingFile $ScriptInfo.TrackingFile -ScriptName $ScriptInfo.Name
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
                Write-ColorBox "  ❌ Failed with exit code: $exitCode" -Color $Colors.Error
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
            Write-ColorBox "  ❌ Exception occurred: $($_.Exception.Message)" -Color $Colors.Error
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
        $statusIcon = if ($result.Status -eq "Success") { "✅" } elseif ($result.Status -eq "Failed") { "❌" } else { "⚠️" }
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
                            DETAILED RESULTS BY STEP
================================================================================

"@
    
    # Add detailed results from each tracking file
    for ($i = 0; $i -lt $Scripts.Count; $i++) {
        $script = $Scripts[$i]
        $report += @"
[$($i + 1)] $($script.Title)
$("-" * 80)
"@
        
        # Read tracking file
        $trackingPath = Join-Path $ScriptDir $script.TrackingFile
        $tracking = Read-JsonReport -FilePath $trackingPath
        
        if ($tracking) {
            $report += "`nTracking File: $($script.TrackingFile)`n"
            
            switch ($script.Name) {
                "convert_images.py" {
                    if ($tracking.processed_images) {
                        $report += "Imported Images: $($tracking.processed_images.Count)`n`n"
                        if ($tracking.processed_images.Count -gt 0) {
                            $report += "Image List:`n"
                            foreach ($img in $tracking.processed_images) {
                                $report += "  • $img`n"
                            }
                        }
                    }
                }
                "images-renamer.py" {
                    if ($tracking.PSObject.Properties.Name -contains 'old_name' -or $tracking.Count -gt 0) {
                        $count = ($tracking.PSObject.Properties | Measure-Object).Count
                        $report += "Renamed Images: $count`n`n"
                        if ($count -gt 0) {
                            $report += "Rename Mapping:`n"
                            foreach ($prop in $tracking.PSObject.Properties) {
                                $report += "  • $($prop.Name) → $($prop.Value)`n"
                            }
                        }
                    }
                }
                default {
                    if ($tracking.processed_files) {
                        $report += "Processed Files: $($tracking.processed_files.Count)`n`n"
                        if ($tracking.processed_files.Count -gt 0) {
                            $report += "File List:`n"
                            foreach ($file in $tracking.processed_files) {
                                $report += "  • $file`n"
                            }
                        }
                    }
                }
            }
            
            if ($tracking.last_run) {
                $report += "`nLast Run: $($tracking.last_run)`n"
            }
        }
        else {
            $report += "`nNo tracking data available.`n"
        }
        
        # Add reference to detailed report file
        $reportFilePath = Join-Path $ScriptDir $script.ReportFile
        if (Test-Path $reportFilePath) {
            $report += "`nDetailed Report: $($script.ReportFile)`n"
        }
        
        $report += "`n"
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
        Write-ColorBox "⚠️  Warning: Could not write report file: $($_.Exception.Message)" -Color $Colors.Warning
        return $null
    }
}

function Show-FinalSummary {
    param([string]$ReportPath)
    
    Write-Host ""
    Write-Host ""
    Write-ColorHeader "EXECUTION SUMMARY" -Color 'Green'
    
    $endTime = Get-Date
    $totalDuration = ($endTime - $GlobalStats.StartTime).TotalSeconds
    
    Write-Host "  ╔════════════════════════════════════════════════════════════════════════╗" -ForegroundColor Green
    Write-Host "  ║  " -NoNewline -ForegroundColor Green
    Write-Host "Pipeline Execution Completed                                        " -NoNewline -ForegroundColor White
    Write-Host "║" -ForegroundColor Green
    Write-Host "  ╚════════════════════════════════════════════════════════════════════════╝" -ForegroundColor Green
    Write-Host ""
    
    # Statistics
    Write-Host "  📊 Statistics:" -ForegroundColor $Colors.Highlight
    Write-Host ""
    Write-ColorBox "     ⏱️  Total Duration: $([math]::Round($totalDuration, 2)) seconds" -Color $Colors.Info
    Write-ColorBox "     📝 Total Steps: $($GlobalStats.TotalSteps)" -Color $Colors.Info
    Write-ColorBox "     ✅ Completed: $($GlobalStats.CompletedSteps)" -Color $Colors.Success
    
    if ($GlobalStats.FailedSteps -gt 0) {
        Write-ColorBox "     ❌ Failed: $($GlobalStats.FailedSteps)" -Color $Colors.Error
    }
    
    $successRate = if($GlobalStats.TotalSteps -gt 0){[math]::Round($GlobalStats.CompletedSteps / $GlobalStats.TotalSteps * 100, 2)}else{0}
    Write-ColorBox "     📈 Success Rate: $successRate%" -Color $(if($successRate -eq 100){'Green'}else{'Yellow'})
    
    Write-Host ""
    
    # Step results
    Write-Host "  📋 Step Results:" -ForegroundColor $Colors.Highlight
    Write-Host ""
    
    foreach ($result in $GlobalStats.StepResults) {
        $statusIcon = if ($result.Status -eq "Success") { "✅" } elseif ($result.Status -eq "Failed") { "❌" } else { "⚠️" }
        $statusColor = if ($result.Status -eq "Success") { $Colors.Success } elseif ($result.Status -eq "Failed") { $Colors.Error } else { $Colors.Warning }
        
        Write-Host "     $statusIcon Step $($result.Step): " -NoNewline -ForegroundColor $statusColor
        Write-Host "$($result.Title) " -NoNewline -ForegroundColor White
        Write-Host "($([math]::Round($result.Duration, 2))s)" -ForegroundColor Gray
    }
    
    Write-Host ""
    Write-Host ""
    
    # Report file
    if ($ReportPath) {
        Write-Host "  📄 Detailed Report:" -ForegroundColor $Colors.Highlight
        Write-Host ""
        Write-ColorBox "     📁 Report saved to: $ReportPath" -Color $Colors.Success
        Write-Host ""
    }
    
    # Final status
    if ($GlobalStats.FailedSteps -eq 0) {
        Write-Host "  " -NoNewline
        Write-Host "╔══════════════════════════════════════════════════════════════════════════╗" -ForegroundColor Green
        Write-Host "  " -NoNewline
        Write-Host "║  " -NoNewline -ForegroundColor Green
        Write-Host "🎉 All Steps Completed Successfully!" -NoNewline -ForegroundColor White
        Write-Host "                                  ║" -ForegroundColor Green
        Write-Host "  " -NoNewline
        Write-Host "╚══════════════════════════════════════════════════════════════════════════╝" -ForegroundColor Green
    }
    else {
        Write-Host "  " -NoNewline
        Write-Host "╔══════════════════════════════════════════════════════════════════════════╗" -ForegroundColor Yellow
        Write-Host "  " -NoNewline
        Write-Host "║  " -NoNewline -ForegroundColor Yellow
        Write-Host "⚠️  Pipeline completed with $($GlobalStats.FailedSteps) failed step(s)" -NoNewline -ForegroundColor White
        Write-Host "                       ║" -ForegroundColor Yellow
        Write-Host "  " -NoNewline
        Write-Host "╚══════════════════════════════════════════════════════════════════════════╝" -ForegroundColor Yellow
    }
    
    Write-Host ""
}

# ============================================================================
# MAIN EXECUTION
# ============================================================================

# Simple mode flag - set to $true for batch-like execution
$SimpleMode = $false

# Check for simple mode parameter
if ($args -contains "-simple") {
    $SimpleMode = $true
}

# Clear screen for better visualization
if (-not $SimpleMode) {
    Clear-Host
}

# Show main header
if (-not $SimpleMode) {
    Write-Host ""
    Write-Host "################################################################################" -ForegroundColor Cyan
    Write-Host "#                                                                              #" -ForegroundColor Cyan
    Write-Host "#          HUGO ARTICLE PROCESSING PIPELINE - ENHANCED VERSION                #" -ForegroundColor Cyan
    Write-Host "#                                                                              #" -ForegroundColor Cyan
    Write-Host "################################################################################" -ForegroundColor Cyan
    Write-Host ""
    Write-ColorBox "📅 Start Time: $($GlobalStats.StartTime.ToString("yyyy-MM-dd HH:mm:ss"))" -Color $Colors.Info
    Write-ColorBox "📂 Working Directory: $ScriptDir" -Color $Colors.Info
    Write-ColorBox "🐍 Python Scripts: $($Scripts.Count)" -Color $Colors.Info
    Write-Host ""

    # Confirm execution
    Write-Host "  " -NoNewline
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
    if (-not $success) {
        Write-Host ""
        Write-ColorBox "  ⚠️  Step $($i + 1) failed. Continue with next step? (Y/N)" -Color $Colors.Warning
        $response = Read-Host "  "
        if ($response -ne 'Y' -and $response -ne 'y') {
            Write-ColorBox "  ❌ Pipeline execution cancelled by user." -Color $Colors.Error
            break
        }
    }
    
    # Small delay between steps for readability
    Start-Sleep -Milliseconds 500
}

# Complete progress
Write-Progress -Activity "Hugo Article Processing Pipeline" -Status "Completed" -PercentComplete 100 -Completed

# Generate final report
Write-Host ""
Write-ColorBox "📝 Generating comprehensive report..." -Color $Colors.Info
$reportPath = Generate-FinalReport

# Show final summary
if (-not $SimpleMode) {
    Show-FinalSummary -ReportPath $reportPath
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
