# ============================================================================
# Hugo Article Import & Image Property Fixer Pipeline
# ============================================================================
# Description: Automated pipeline for importing articles and fixing images
# Author: Davoodya Team
# Date: 2026-02-10
# Version: 2.0 (Fixed & Enhanced)
# ============================================================================

# Set encoding to UTF-8 for proper display
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

# Get script directory dynamically
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

# ============================================================================
# CONFIGURATION
# ============================================================================

# Pipeline Steps Configuration
$Scripts = @(
    @{
        Step = 1
        Name = "convert_images.py"
        Title = "Import New Articles Images"
        Description = "Import images from Obsidian Vault to Hugo static/images"
        ReportFile = "image_migration_report.txt"
    },
    @{
        Step = 2
        Name = "title-adder.py"
        Title = "Add Title for New Articles"
        Description = "Add Hugo front matter title based on filename"
        ReportFile = "title_adder_report.txt"
        Note = "Required for next steps (image renaming)"
    },
    @{
        Step = 3
        Name = "altimage-adder.py"
        Title = "Add ALT for Images"
        Description = "Add ALT attributes to images based on article title"
        ReportFile = "altimage_adder_report.txt"
    },
    @{
        Step = 4
        Name = "images-renamer.py"
        Title = "Rename Images in /static/images"
        Description = "Rename images using slugified names"
        ReportFile = "images_renamer_report.txt"
    },
    @{
        Step = 5
        Name = "image-article-renamer.py"
        Title = "Update Image References"
        Description = "Update image paths in articles with new names"
        ReportFile = "image_article_renamer_report.txt"
    },
    @{
        Step = 6
        Name = "toc-remover.py"
        Title = "Remove Obsidian TOC"
        Description = "Remove Obsidian Table of Contents from articles"
        ReportFile = "toc_remover_report.txt"
    },
    @{
        Step = 7
        Name = "obsidian-property-remover-enhanced.py"
        Title = "Add Enhanced Hugo Front Matter"
        Description = "Add comprehensive Hugo properties to articles"
        ReportFile = "obsidian_property_remover_enhanced_report.txt"
    }
)

# Global Statistics
$GlobalStats = @{
    StartTime = Get-Date
    TotalSteps = $Scripts.Count
    CompletedSteps = 0
    FailedSteps = 0
    SkippedSteps = 0
    StepResults = @()
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

function Write-BoxedTitle {
    param([string]$Title)
    
    $width = 80
    $line = "=" * $width
    $padding = " " * [Math]::Max(0, [Math]::Floor(($width - $Title.Length) / 2))
    
    Write-Host ""
    Write-Host $line -ForegroundColor Cyan
    Write-Host "$padding$Title" -ForegroundColor White
    Write-Host $line -ForegroundColor Cyan
    Write-Host ""
}

function Write-StepHeader {
    param(
        [int]$StepNumber,
        [hashtable]$ScriptInfo
    )
    
    Write-Host ""
    Write-Host ("=" * 80) -ForegroundColor Cyan
    Write-Host "STEP $StepNumber of $($GlobalStats.TotalSteps): $($ScriptInfo.Title)" -ForegroundColor White
    Write-Host ("=" * 80) -ForegroundColor Cyan
    Write-Host "Description: $($ScriptInfo.Description)" -ForegroundColor Gray
    Write-Host "Script:      $($ScriptInfo.Name)" -ForegroundColor Gray
    
    if ($ScriptInfo.Note) {
        Write-Host "Note:        $($ScriptInfo.Note)" -ForegroundColor Yellow
    }
    
    Write-Host ""
}

function Write-StatusMessage {
    param(
        [string]$Message,
        [string]$Type = "Info"
    )
    
    $color = switch ($Type) {
        "Success" { "Green" }
        "Error" { "Red" }
        "Warning" { "Yellow" }
        "Info" { "Cyan" }
        default { "White" }
    }
    
    $icon = switch ($Type) {
        "Success" { "[OK]" }
        "Error" { "[ERROR]" }
        "Warning" { "[WARN]" }
        "Info" { "[INFO]" }
        default { "[*]" }
    }
    
    Write-Host "$icon $Message" -ForegroundColor $color
}

function Test-PythonScript {
    param([string]$ScriptPath)
    
    if (-not (Test-Path $ScriptPath)) {
        return $false
    }
    
    # Try to parse Python file for syntax errors (basic check)
    try {
        $content = Get-Content $ScriptPath -Raw -ErrorAction Stop
        return $true
    }
    catch {
        return $false
    }
}

function Execute-PythonScript {
    param(
        [hashtable]$ScriptInfo
    )
    
    $scriptPath = Join-Path $ScriptDir $ScriptInfo.Name
    $stepNumber = $ScriptInfo.Step
    
    # Show step header
    Write-StepHeader -StepNumber $stepNumber -ScriptInfo $ScriptInfo
    
    # Check if script exists
    if (-not (Test-Path $scriptPath)) {
        Write-StatusMessage "Script not found: $($ScriptInfo.Name)" "Error"
        
        $GlobalStats.FailedSteps++
        $GlobalStats.StepResults += @{
            Step = $stepNumber
            Name = $ScriptInfo.Name
            Title = $ScriptInfo.Title
            Status = "Failed"
            Reason = "Script not found"
            Duration = 0
        }
        
        return $false
    }
    
    Write-StatusMessage "Starting execution..." "Info"
    Write-Host ""
    
    $startTime = Get-Date
    
    try {
        # Execute Python script and capture output
        Write-Host ("-" * 80) -ForegroundColor DarkGray
        
        # Run Python with proper error handling
        $process = Start-Process -FilePath "python.exe" `
            -ArgumentList "`"$scriptPath`"" `
            -NoNewWindow `
            -Wait `
            -PassThru `
            -RedirectStandardOutput "$env:TEMP\py_stdout.txt" `
            -RedirectStandardError "$env:TEMP\py_stderr.txt"
        
        $exitCode = $process.ExitCode
        
        # Display output
        if (Test-Path "$env:TEMP\py_stdout.txt") {
            $output = Get-Content "$env:TEMP\py_stdout.txt" -Raw
            if ($output) {
                # Filter and show relevant lines
                $lines = $output -split "`n"
                foreach ($line in $lines) {
                    if ($line -match "(ERROR|FAIL|WARNING|SUCCESS|COMPLETED|processed|found|Step|Total)" -or 
                        $line.Trim().Length -lt 100) {
                        Write-Host $line
                    }
                }
            }
            Remove-Item "$env:TEMP\py_stdout.txt" -ErrorAction SilentlyContinue
        }
        
        # Show errors if any
        if (Test-Path "$env:TEMP\py_stderr.txt") {
            $errors = Get-Content "$env:TEMP\py_stderr.txt" -Raw
            if ($errors -and $errors.Trim()) {
                Write-Host ""
                Write-Host "Errors/Warnings:" -ForegroundColor Yellow
                Write-Host $errors -ForegroundColor Yellow
            }
            Remove-Item "$env:TEMP\py_stderr.txt" -ErrorAction SilentlyContinue
        }
        
        Write-Host ("-" * 80) -ForegroundColor DarkGray
        Write-Host ""
        
        $endTime = Get-Date
        $duration = ($endTime - $startTime).TotalSeconds
        
        # Check exit code
        if ($exitCode -eq 0) {
            Write-StatusMessage "Completed successfully in $([math]::Round($duration, 2))s" "Success"
            
            $GlobalStats.CompletedSteps++
            $GlobalStats.StepResults += @{
                Step = $stepNumber
                Name = $ScriptInfo.Name
                Title = $ScriptInfo.Title
                Status = "Success"
                Duration = $duration
                ExitCode = $exitCode
            }
            
            return $true
        }
        else {
            Write-StatusMessage "Failed with exit code: $exitCode" "Error"
            
            $GlobalStats.FailedSteps++
            $GlobalStats.StepResults += @{
                Step = $stepNumber
                Name = $ScriptInfo.Name
                Title = $ScriptInfo.Title
                Status = "Failed"
                Duration = $duration
                ExitCode = $exitCode
                Reason = "Non-zero exit code"
            }
            
            return $false
        }
    }
    catch {
        Write-StatusMessage "Exception: $($_.Exception.Message)" "Error"
        
        $GlobalStats.FailedSteps++
        $GlobalStats.StepResults += @{
            Step = $stepNumber
            Name = $ScriptInfo.Name
            Title = $ScriptInfo.Title
            Status = "Error"
            Duration = 0
            ExitCode = -1
            Reason = $_.Exception.Message
        }
        
        return $false
    }
}

function Generate-FinalReport {
    $reportPath = Join-Path $ScriptDir "pipeline-execution-report.txt"
    $endTime = Get-Date
    $totalDuration = ($endTime - $GlobalStats.StartTime).TotalSeconds
    
    $report = @"
================================================================================
              HUGO ARTICLE IMPORT & IMAGE PROPERTY FIXER REPORT
================================================================================

Execution Summary
--------------------------------------------------------------------------------
Start Time:           $($GlobalStats.StartTime.ToString("yyyy-MM-dd HH:mm:ss"))
End Time:             $($endTime.ToString("yyyy-MM-dd HH:mm:ss"))
Total Duration:       $([math]::Round($totalDuration, 2)) seconds
Total Steps:          $($GlobalStats.TotalSteps)
Completed Steps:      $($GlobalStats.CompletedSteps)
Failed Steps:         $($GlobalStats.FailedSteps)
Skipped Steps:        $($GlobalStats.SkippedSteps)
Success Rate:         $(if($GlobalStats.TotalSteps -gt 0){[math]::Round($GlobalStats.CompletedSteps / $GlobalStats.TotalSteps * 100, 2)}else{0})%

================================================================================
                          PIPELINE STEPS DETAILS
================================================================================

"@
    
    foreach ($result in $GlobalStats.StepResults) {
        $statusSymbol = switch ($result.Status) {
            "Success" { "OK" }
            "Failed" { "FAIL" }
            "Error" { "ERROR" }
            "Skipped" { "SKIP" }
            default { "?" }
        }
        
        $report += @"
Step $($result.Step): $($result.Title)
$("-" * 80)
Script:         $($result.Name)
Status:         [$statusSymbol] $($result.Status)
Duration:       $([math]::Round($result.Duration, 2))s
Exit Code:      $($result.ExitCode)

"@
        
        if ($result.Reason) {
            $report += "Reason:         $($result.Reason)`n`n"
        }
    }
    
    $report += @"
================================================================================
                            STEP-BY-STEP SUMMARY
================================================================================

1. Import New Articles Images
   - Source: Obsidian Vault Attachment folder
   - Destination: static/images/[category]/
   - Process: Copy new images only (skips existing)
   
2. Add Title for New Articles
   - Adds 'title = "Article Name"' to Hugo front matter
   - Removes E-numbers from filename (E3, E45, etc.)
   - REQUIRED: This step is essential for Steps 3, 4, 5

3. Add ALT for Images in Articles
   - Adds ALT attributes to all images
   - ALT text based on article title property
   - Improves SEO and accessibility

4. Rename Images in /static/images
   - Renames all images with slugified names
   - Format: lowercase-with-dashes.extension
   - Example: "My Image.png" -> "my-image.png"

5. Update Image References in Articles
   - Updates all image paths in markdown files
   - Matches new names from Step 4
   - Ensures all references are synchronized

6. Remove Obsidian TOC from Articles
   - Removes Obsidian's Table of Contents sections
   - Hugo will generate its own TOC
   - Cleans up markdown structure

7. Add Enhanced Hugo Front Matter
   - Adds comprehensive front matter properties
   - Includes: title, slug, date, categories, tags
   - Also adds: SEO, Open Graph, Twitter Cards, reading time
   - Removes old Obsidian properties

================================================================================
                             INDIVIDUAL REPORTS
================================================================================

Each step generates its own detailed report file:

"@
    
    foreach ($script in $Scripts) {
        $reportFile = Join-Path $ScriptDir $script.ReportFile
        $exists = Test-Path $reportFile
        $status = if ($exists) { "Available" } else { "Not Generated" }
        
        $report += "Step $($script.Step): $($script.ReportFile) - $status`n"
    }
    
    $report += @"

================================================================================
                                  NOTES
================================================================================

- All scripts use tracking files to avoid re-processing files
- Only new/modified files are processed in subsequent runs
- Each script generates its own detailed report
- Check individual report files for specific details

================================================================================
                                END OF REPORT
================================================================================

Report generated: $($endTime.ToString("yyyy-MM-dd HH:mm:ss"))
Report location: $reportPath

"@
    
    # Write report to file
    try {
        $report | Out-File -FilePath $reportPath -Encoding UTF8 -Force
        return $reportPath
    }
    catch {
        Write-StatusMessage "Could not write report file: $($_.Exception.Message)" "Warning"
        return $null
    }
}

function Show-FinalSummary {
    param([string]$ReportPath)
    
    Write-Host ""
    Write-Host ""
    Write-BoxedTitle "EXECUTION SUMMARY"
    
    $endTime = Get-Date
    $totalDuration = ($endTime - $GlobalStats.StartTime).TotalSeconds
    
    # Overall Status
    Write-Host "Pipeline Execution Completed" -ForegroundColor White
    Write-Host ""
    
    # Duration
    Write-Host "Duration:     " -NoNewline
    Write-Host "$([math]::Round($totalDuration, 2)) seconds" -ForegroundColor Cyan
    
    # Steps Summary
    Write-Host "Total Steps:  " -NoNewline
    Write-Host "$($GlobalStats.TotalSteps)" -ForegroundColor White
    
    Write-Host "Completed:    " -NoNewline
    Write-Host "$($GlobalStats.CompletedSteps)" -ForegroundColor Green
    
    if ($GlobalStats.FailedSteps -gt 0) {
        Write-Host "Failed:       " -NoNewline
        Write-Host "$($GlobalStats.FailedSteps)" -ForegroundColor Red
    }
    
    if ($GlobalStats.SkippedSteps -gt 0) {
        Write-Host "Skipped:      " -NoNewline
        Write-Host "$($GlobalStats.SkippedSteps)" -ForegroundColor Yellow
    }
    
    # Success Rate
    $successRate = if($GlobalStats.TotalSteps -gt 0){
        [math]::Round($GlobalStats.CompletedSteps / $GlobalStats.TotalSteps * 100, 2)
    }else{0}
    
    Write-Host "Success Rate: " -NoNewline
    $rateColor = if($successRate -eq 100){'Green'}elseif($successRate -ge 80){'Yellow'}else{'Red'}
    Write-Host "$successRate%" -ForegroundColor $rateColor
    
    Write-Host ""
    Write-Host ("-" * 80) -ForegroundColor Gray
    Write-Host ""
    
    # Step Results Table
    Write-Host "STEP RESULTS:" -ForegroundColor Yellow
    Write-Host ""
    
    foreach ($result in $GlobalStats.StepResults) {
        $statusColor = switch ($result.Status) {
            "Success" { "Green" }
            "Failed" { "Red" }
            "Error" { "Red" }
            "Skipped" { "Yellow" }
            default { "White" }
        }
        
        $statusSymbol = switch ($result.Status) {
            "Success" { "OK" }
            "Failed" { "FAIL" }
            "Error" { "ERR" }
            "Skipped" { "SKIP" }
            default { "?" }
        }
        
        $duration = [math]::Round($result.Duration, 1)
        Write-Host "  [$statusSymbol] " -NoNewline -ForegroundColor $statusColor
        Write-Host "Step $($result.Step): " -NoNewline
        Write-Host "$($result.Title) " -NoNewline -ForegroundColor White
        Write-Host "($($duration)s)" -ForegroundColor Gray
    }
    
    Write-Host ""
    Write-Host ("-" * 80) -ForegroundColor Gray
    Write-Host ""
    
    # Report File
    if ($ReportPath) {
        Write-Host "DETAILED REPORT:" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "  $ReportPath" -ForegroundColor Green
        Write-Host ""
    }
    
    # Final Status Message
    Write-Host ""
    if ($GlobalStats.FailedSteps -eq 0) {
        Write-Host "All Steps Completed Successfully!" -ForegroundColor Green
        Write-Host "All images imported and properties fixed." -ForegroundColor Green
    }
    else {
        Write-Host "Pipeline completed with $($GlobalStats.FailedSteps) failed step(s)." -ForegroundColor Yellow
        Write-Host "Check the report for details." -ForegroundColor Yellow
    }
    
    Write-Host ""
}

# ============================================================================
# MAIN EXECUTION
# ============================================================================

# Clear screen
Clear-Host

# Show header
Write-BoxedTitle "HUGO ARTICLE IMPORT & IMAGE PROPERTY FIXER PIPELINE"

Write-Host "Start Time:       $($GlobalStats.StartTime.ToString("yyyy-MM-dd HH:mm:ss"))" -ForegroundColor White
Write-Host "Working Directory: $ScriptDir" -ForegroundColor White
Write-Host "Total Steps:      $($Scripts.Count)" -ForegroundColor White
Write-Host ""

# Verify all scripts exist
Write-StatusMessage "Verifying Python scripts..." "Info"
$allScriptsExist = $true
foreach ($script in $Scripts) {
    $scriptPath = Join-Path $ScriptDir $script.Name
    if (-not (Test-Path $scriptPath)) {
        Write-StatusMessage "Missing: $($script.Name)" "Error"
        $allScriptsExist = $false
    }
    else {
        Write-Host "  [OK] $($script.Name)" -ForegroundColor Green
    }
}

if (-not $allScriptsExist) {
    Write-Host ""
    Write-StatusMessage "Some scripts are missing. Cannot continue." "Error"
    Write-Host ""
    pause
    exit 1
}

Write-Host ""
Write-StatusMessage "All scripts found. Ready to execute." "Success"
Write-Host ""

# Confirm execution
Write-Host "Press any key to start pipeline execution..." -ForegroundColor Yellow
Write-Host "(or Ctrl+C to cancel)" -ForegroundColor Gray
Write-Host ""

try {
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
}
catch {
    # Auto-start for non-interactive environments
    Write-StatusMessage "Auto-starting in 3 seconds..." "Info"
    Start-Sleep -Seconds 3
}

# Execute all scripts in sequence
foreach ($script in $Scripts) {
    $success = Execute-PythonScript -ScriptInfo $script
    
    # If a step fails, ask to continue
    if (-not $success) {
        Write-Host ""
        Write-Host "Step $($script.Step) failed. Continue with next step? (Y/N): " -NoNewline -ForegroundColor Yellow
        $response = Read-Host
        
        if ($response -ne 'Y' -and $response -ne 'y') {
            Write-StatusMessage "Pipeline execution cancelled by user." "Warning"
            $GlobalStats.SkippedSteps = $GlobalStats.TotalSteps - $script.Step
            break
        }
        
        Write-StatusMessage "Continuing with next step..." "Info"
    }
    
    # Small delay for readability
    Start-Sleep -Milliseconds 300
}

# Generate comprehensive report
Write-Host ""
Write-StatusMessage "Generating final report..." "Info"
$reportPath = Generate-FinalReport

# Show final summary
Show-FinalSummary -ReportPath $reportPath

# Footer
Write-Host ""
Write-Host ("=" * 80) -ForegroundColor Cyan
Write-Host ""

# Keep window open
Write-Host "Press any key to exit..." -ForegroundColor Gray
try {
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
}
catch {
    # Fallback
    pause
}
