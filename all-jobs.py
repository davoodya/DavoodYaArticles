#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
Hugo Article Import & Image Property Fixer Pipeline
================================================================================
Description: Automated pipeline for importing articles and fixing images
Author: Davoodya Team
Date: 2026-02-10
Version: 2.0 (Python Edition)
================================================================================
"""

import os
import sys
import subprocess
import time
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple

# ANSI Color Codes for terminal output
class Colors:
    """ANSI color codes for beautiful terminal output"""
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[97m'
    GRAY = '\033[90m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    
    @staticmethod
    def colored(text: str, color: str) -> str:
        """Return colored text"""
        return f"{color}{text}{Colors.RESET}"


# ============================================================================
# CONFIGURATION
# ============================================================================

# Pipeline Steps Configuration
PIPELINE_STEPS = [
    {
        'step': 1,
        'name': 'convert_images.py',
        'title': 'Import New Articles Images',
        'description': 'Import images from Obsidian Vault to Hugo static/images',
        'report_file': 'image_migration_report.txt'
    },
    {
        'step': 2,
        'name': 'title-adder.py',
        'title': 'Add Title for New Articles',
        'description': 'Add Hugo front matter title based on filename',
        'report_file': 'title_adder_report.txt',
        'note': 'Required for next steps (image renaming)'
    },
    {
        'step': 3,
        'name': 'altimage-adder.py',
        'title': 'Add ALT for Images',
        'description': 'Add ALT attributes to images based on article title',
        'report_file': 'altimage_adder_report.txt'
    },
    {
        'step': 4,
        'name': 'images-renamer.py',
        'title': 'Rename Images in /static/images',
        'description': 'Rename images using slugified names',
        'report_file': 'images_renamer_report.txt'
    },
    {
        'step': 5,
        'name': 'image-article-renamer.py',
        'title': 'Update Image References',
        'description': 'Update image paths in articles with new names',
        'report_file': 'image_article_renamer_report.txt'
    },
    {
        'step': 6,
        'name': 'toc-remover.py',
        'title': 'Remove Obsidian TOC',
        'description': 'Remove Obsidian Table of Contents from articles',
        'report_file': 'toc_remover_report.txt'
    },
    {
        'step': 7,
        'name': 'obsidian-property-remover-enhanced.py',
        'title': 'Add Enhanced Hugo Front Matter',
        'description': 'Add comprehensive Hugo properties to articles',
        'report_file': 'obsidian_property_remover_enhanced_report.txt'
    }
]

# Global Statistics
class PipelineStats:
    """Global statistics for pipeline execution"""
    def __init__(self):
        self.start_time = datetime.now()
        self.end_time = None
        self.total_steps = len(PIPELINE_STEPS)
        self.completed_steps = 0
        self.failed_steps = 0
        self.skipped_steps = 0
        self.step_results = []
    
    def get_duration(self) -> float:
        """Get total duration in seconds"""
        end = self.end_time or datetime.now()
        return (end - self.start_time).total_seconds()
    
    def get_success_rate(self) -> float:
        """Calculate success rate percentage"""
        if self.total_steps == 0:
            return 0.0
        return round((self.completed_steps / self.total_steps) * 100, 2)


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_boxed_title(title: str, width: int = 80):
    """Print a boxed title with borders"""
    line = "=" * width
    padding = " " * max(0, (width - len(title)) // 2)
    
    print()
    print(Colors.colored(line, Colors.CYAN))
    print(Colors.colored(f"{padding}{title}", Colors.WHITE))
    print(Colors.colored(line, Colors.CYAN))
    print()


def print_step_header(step_info: Dict, total_steps: int):
    """Print step header with details"""
    step_num = step_info['step']
    
    print()
    print(Colors.colored("=" * 80, Colors.CYAN))
    print(Colors.colored(f"STEP {step_num} of {total_steps}: {step_info['title']}", Colors.WHITE))
    print(Colors.colored("=" * 80, Colors.CYAN))
    print(Colors.colored(f"Description: {step_info['description']}", Colors.GRAY))
    print(Colors.colored(f"Script:      {step_info['name']}", Colors.GRAY))
    
    if 'note' in step_info:
        print(Colors.colored(f"Note:        {step_info['note']}", Colors.YELLOW))
    
    print()


def print_status_message(message: str, msg_type: str = "info"):
    """Print colored status message with icon"""
    colors = {
        'success': Colors.GREEN,
        'error': Colors.RED,
        'warning': Colors.YELLOW,
        'info': Colors.CYAN
    }
    
    icons = {
        'success': '[OK]',
        'error': '[ERROR]',
        'warning': '[WARN]',
        'info': '[INFO]'
    }
    
    color = colors.get(msg_type.lower(), Colors.WHITE)
    icon = icons.get(msg_type.lower(), '[*]')
    
    print(Colors.colored(f"{icon} {message}", color))


def get_script_directory() -> Path:
    """Get the directory where this script is located"""
    return Path(__file__).parent.absolute()


def test_python_script(script_path: Path) -> bool:
    """Test if Python script exists and is readable"""
    if not script_path.exists():
        return False
    
    try:
        with open(script_path, 'r', encoding='utf-8') as f:
            f.read(100)  # Read first 100 chars as basic check
        return True
    except Exception:
        return False


def execute_python_script(step_info: Dict, script_dir: Path) -> Tuple[bool, Dict]:
    """
    Execute a Python script and return success status and result info
    
    Returns:
        Tuple[bool, Dict]: (success, result_dict)
    """
    script_path = script_dir / step_info['name']
    step_num = step_info['step']
    
    # Show step header
    print_step_header(step_info, len(PIPELINE_STEPS))
    
    # Check if script exists
    if not script_path.exists():
        print_status_message(f"Script not found: {step_info['name']}", "error")
        
        result = {
            'step': step_num,
            'name': step_info['name'],
            'title': step_info['title'],
            'status': 'Failed',
            'reason': 'Script not found',
            'duration': 0,
            'exit_code': -1
        }
        
        return False, result
    
    print_status_message("Starting execution...", "info")
    print()
    
    start_time = time.time()
    
    try:
        # Execute Python script
        print(Colors.colored("-" * 80, Colors.GRAY))
        
        # Run script with subprocess
        result_proc = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace'
        )
        
        exit_code = result_proc.returncode
        
        # Display output (filtered)
        if result_proc.stdout:
            lines = result_proc.stdout.split('\n')
            for line in lines:
                # Show important lines
                if any(keyword in line for keyword in [
                    'ERROR', 'FAIL', 'WARNING', 'SUCCESS', 'COMPLETED',
                    'processed', 'found', 'Step', 'Total'
                ]) or len(line.strip()) < 100:
                    print(line)
        
        # Show errors if any
        if result_proc.stderr and result_proc.stderr.strip():
            print()
            print(Colors.colored("Errors/Warnings:", Colors.YELLOW))
            print(Colors.colored(result_proc.stderr, Colors.YELLOW))
        
        print(Colors.colored("-" * 80, Colors.GRAY))
        print()
        
        end_time = time.time()
        duration = end_time - start_time
        
        # Check exit code
        if exit_code == 0:
            print_status_message(f"Completed successfully in {duration:.2f}s", "success")
            
            result = {
                'step': step_num,
                'name': step_info['name'],
                'title': step_info['title'],
                'status': 'Success',
                'duration': duration,
                'exit_code': exit_code
            }
            
            return True, result
        else:
            print_status_message(f"Failed with exit code: {exit_code}", "error")
            
            result = {
                'step': step_num,
                'name': step_info['name'],
                'title': step_info['title'],
                'status': 'Failed',
                'duration': duration,
                'exit_code': exit_code,
                'reason': 'Non-zero exit code'
            }
            
            return False, result
            
    except Exception as e:
        print_status_message(f"Exception: {str(e)}", "error")
        
        result = {
            'step': step_num,
            'name': step_info['name'],
            'title': step_info['title'],
            'status': 'Error',
            'duration': 0,
            'exit_code': -1,
            'reason': str(e)
        }
        
        return False, result


def generate_final_report(stats: PipelineStats, script_dir: Path) -> Optional[str]:
    """
    Generate comprehensive final report
    
    Returns:
        Optional[str]: Path to report file, or None if failed
    """
    report_path = script_dir / "pipeline-execution-report.txt"
    
    try:
        with open(report_path, 'w', encoding='utf-8') as f:
            # Header
            f.write("=" * 80 + "\n")
            f.write("              HUGO ARTICLE IMPORT & IMAGE PROPERTY FIXER REPORT\n")
            f.write("=" * 80 + "\n\n")
            
            # Execution Summary
            f.write("Execution Summary\n")
            f.write("-" * 80 + "\n")
            f.write(f"Start Time:           {stats.start_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"End Time:             {stats.end_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total Duration:       {stats.get_duration():.2f} seconds\n")
            f.write(f"Total Steps:          {stats.total_steps}\n")
            f.write(f"Completed Steps:      {stats.completed_steps}\n")
            f.write(f"Failed Steps:         {stats.failed_steps}\n")
            f.write(f"Skipped Steps:        {stats.skipped_steps}\n")
            f.write(f"Success Rate:         {stats.get_success_rate()}%\n\n")
            
            # Pipeline Steps Details
            f.write("=" * 80 + "\n")
            f.write("                          PIPELINE STEPS DETAILS\n")
            f.write("=" * 80 + "\n\n")
            
            for result in stats.step_results:
                status_symbol = {
                    'Success': 'OK',
                    'Failed': 'FAIL',
                    'Error': 'ERROR',
                    'Skipped': 'SKIP'
                }.get(result['status'], '?')
                
                f.write(f"Step {result['step']}: {result['title']}\n")
                f.write("-" * 80 + "\n")
                f.write(f"Script:         {result['name']}\n")
                f.write(f"Status:         [{status_symbol}] {result['status']}\n")
                f.write(f"Duration:       {result['duration']:.2f}s\n")
                f.write(f"Exit Code:      {result['exit_code']}\n")
                
                if 'reason' in result:
                    f.write(f"Reason:         {result['reason']}\n")
                
                f.write("\n")
            
            # Step-by-Step Summary
            f.write("=" * 80 + "\n")
            f.write("                            STEP-BY-STEP SUMMARY\n")
            f.write("=" * 80 + "\n\n")
            
            summaries = [
                ("1. Import New Articles Images", [
                    "- Source: Obsidian Vault Attachment folder",
                    "- Destination: static/images/[category]/",
                    "- Process: Copy new images only (skips existing)"
                ]),
                ("2. Add Title for New Articles", [
                    "- Adds 'title = \"Article Name\"' to Hugo front matter",
                    "- Removes E-numbers from filename (E3, E45, etc.)",
                    "- REQUIRED: This step is essential for Steps 3, 4, 5"
                ]),
                ("3. Add ALT for Images in Articles", [
                    "- Adds ALT attributes to all images",
                    "- ALT text based on article title property",
                    "- Improves SEO and accessibility"
                ]),
                ("4. Rename Images in /static/images", [
                    "- Renames all images with slugified names",
                    "- Format: lowercase-with-dashes.extension",
                    "- Example: \"My Image.png\" -> \"my-image.png\""
                ]),
                ("5. Update Image References in Articles", [
                    "- Updates all image paths in markdown files",
                    "- Matches new names from Step 4",
                    "- Ensures all references are synchronized"
                ]),
                ("6. Remove Obsidian TOC from Articles", [
                    "- Removes Obsidian's Table of Contents sections",
                    "- Hugo will generate its own TOC",
                    "- Cleans up markdown structure"
                ]),
                ("7. Add Enhanced Hugo Front Matter", [
                    "- Adds comprehensive front matter properties",
                    "- Includes: title, slug, date, categories, tags",
                    "- Also adds: SEO, Open Graph, Twitter Cards, reading time",
                    "- Removes old Obsidian properties"
                ])
            ]
            
            for title, points in summaries:
                f.write(f"{title}\n")
                for point in points:
                    f.write(f"   {point}\n")
                f.write("\n")
            
            # Individual Reports
            f.write("=" * 80 + "\n")
            f.write("                             INDIVIDUAL REPORTS\n")
            f.write("=" * 80 + "\n\n")
            f.write("Each step generates its own detailed report file:\n\n")
            
            for step in PIPELINE_STEPS:
                report_file = script_dir / step['report_file']
                status = "Available" if report_file.exists() else "Not Generated"
                f.write(f"Step {step['step']}: {step['report_file']} - {status}\n")
            
            # Notes
            f.write("\n")
            f.write("=" * 80 + "\n")
            f.write("                                  NOTES\n")
            f.write("=" * 80 + "\n\n")
            f.write("- All scripts use tracking files to avoid re-processing files\n")
            f.write("- Only new/modified files are processed in subsequent runs\n")
            f.write("- Each script generates its own detailed report\n")
            f.write("- Check individual report files for specific details\n\n")
            
            # Footer
            f.write("=" * 80 + "\n")
            f.write("                                END OF REPORT\n")
            f.write("=" * 80 + "\n\n")
            f.write(f"Report generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Report location: {report_path}\n\n")
        
        return str(report_path)
        
    except Exception as e:
        print_status_message(f"Could not write report file: {str(e)}", "warning")
        return None


def show_final_summary(stats: PipelineStats, report_path: Optional[str]):
    """Display final execution summary"""
    print()
    print()
    print_boxed_title("EXECUTION SUMMARY")
    
    # Overall Status
    print(Colors.colored("Pipeline Execution Completed", Colors.WHITE))
    print()
    
    # Duration
    print("Duration:     ", end="")
    print(Colors.colored(f"{stats.get_duration():.2f} seconds", Colors.CYAN))
    
    # Steps Summary
    print("Total Steps:  ", end="")
    print(Colors.colored(str(stats.total_steps), Colors.WHITE))
    
    print("Completed:    ", end="")
    print(Colors.colored(str(stats.completed_steps), Colors.GREEN))
    
    if stats.failed_steps > 0:
        print("Failed:       ", end="")
        print(Colors.colored(str(stats.failed_steps), Colors.RED))
    
    if stats.skipped_steps > 0:
        print("Skipped:      ", end="")
        print(Colors.colored(str(stats.skipped_steps), Colors.YELLOW))
    
    # Success Rate
    success_rate = stats.get_success_rate()
    rate_color = Colors.GREEN if success_rate == 100 else (Colors.YELLOW if success_rate >= 80 else Colors.RED)
    print("Success Rate: ", end="")
    print(Colors.colored(f"{success_rate}%", rate_color))
    
    print()
    print(Colors.colored("-" * 80, Colors.GRAY))
    print()
    
    # Step Results Table
    print(Colors.colored("STEP RESULTS:", Colors.YELLOW))
    print()
    
    for result in stats.step_results:
        status_color = {
            'Success': Colors.GREEN,
            'Failed': Colors.RED,
            'Error': Colors.RED,
            'Skipped': Colors.YELLOW
        }.get(result['status'], Colors.WHITE)
        
        status_symbol = {
            'Success': 'OK',
            'Failed': 'FAIL',
            'Error': 'ERR',
            'Skipped': 'SKIP'
        }.get(result['status'], '?')
        
        duration = round(result['duration'], 1)
        
        print(f"  {Colors.colored(f'[{status_symbol}]', status_color)} ", end="")
        print(f"Step {result['step']}: ", end="")
        print(Colors.colored(result['title'], Colors.WHITE), end=" ")
        print(Colors.colored(f"({duration}s)", Colors.GRAY))
    
    print()
    print(Colors.colored("-" * 80, Colors.GRAY))
    print()
    
    # Report File
    if report_path:
        print(Colors.colored("DETAILED REPORT:", Colors.YELLOW))
        print()
        print("  " + Colors.colored(report_path, Colors.GREEN))
        print()
    
    # Final Status Message
    print()
    if stats.failed_steps == 0:
        print(Colors.colored("All Steps Completed Successfully!", Colors.GREEN))
        print(Colors.colored("All images imported and properties fixed.", Colors.GREEN))
    else:
        print(Colors.colored(f"Pipeline completed with {stats.failed_steps} failed step(s).", Colors.YELLOW))
        print(Colors.colored("Check the report for details.", Colors.YELLOW))
    
    print()


def verify_all_scripts(script_dir: Path) -> bool:
    """
    Verify that all Python scripts exist
    
    Returns:
        bool: True if all scripts exist, False otherwise
    """
    print_status_message("Verifying Python scripts...", "info")
    
    all_exist = True
    for step in PIPELINE_STEPS:
        script_path = script_dir / step['name']
        if not script_path.exists():
            print_status_message(f"Missing: {step['name']}", "error")
            all_exist = False
        else:
            print("  " + Colors.colored(f"[OK] {step['name']}", Colors.GREEN))
    
    return all_exist


def get_user_confirmation() -> bool:
    """
    Ask user to confirm execution
    
    Returns:
        bool: True if user confirms, False otherwise
    """
    print()
    print(Colors.colored("Press Enter to start pipeline execution...", Colors.YELLOW))
    print(Colors.colored("(or Ctrl+C to cancel)", Colors.GRAY))
    print()
    
    try:
        input()
        return True
    except KeyboardInterrupt:
        print()
        print_status_message("Cancelled by user.", "warning")
        return False


def ask_continue_after_failure(step_num: int) -> bool:
    """
    Ask user if they want to continue after a step fails
    
    Returns:
        bool: True if user wants to continue, False otherwise
    """
    print()
    print(Colors.colored(f"Step {step_num} failed. Continue with next step? (Y/N): ", Colors.YELLOW), end="")
    
    try:
        response = input().strip().upper()
        return response in ['Y', 'YES']
    except KeyboardInterrupt:
        return False


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main execution function"""
    # Initialize stats
    stats = PipelineStats()
    
    # Get script directory
    script_dir = get_script_directory()
    
    # Clear screen
    clear_screen()
    
    # Show header
    print_boxed_title("HUGO ARTICLE IMPORT & IMAGE PROPERTY FIXER PIPELINE")
    
    print(Colors.colored(f"Start Time:        {stats.start_time.strftime('%Y-%m-%d %H:%M:%S')}", Colors.WHITE))
    print(Colors.colored(f"Working Directory: {script_dir}", Colors.WHITE))
    print(Colors.colored(f"Total Steps:       {stats.total_steps}", Colors.WHITE))
    print()
    
    # Verify all scripts exist
    if not verify_all_scripts(script_dir):
        print()
        print_status_message("Some scripts are missing. Cannot continue.", "error")
        print()
        input("Press Enter to exit...")
        sys.exit(1)
    
    print()
    print_status_message("All scripts found. Ready to execute.", "success")
    print()
    
    # Get user confirmation
    if not get_user_confirmation():
        sys.exit(0)
    
    # Execute all scripts in sequence
    for step in PIPELINE_STEPS:
        success, result = execute_python_script(step, script_dir)
        
        # Add result to stats
        stats.step_results.append(result)
        
        if success:
            stats.completed_steps += 1
        else:
            stats.failed_steps += 1
            
            # Ask to continue
            if not ask_continue_after_failure(step['step']):
                print_status_message("Pipeline execution cancelled by user.", "warning")
                stats.skipped_steps = stats.total_steps - step['step']
                break
            
            print_status_message("Continuing with next step...", "info")
        
        # Small delay for readability
        time.sleep(0.3)
    
    # Set end time
    stats.end_time = datetime.now()
    
    # Generate comprehensive report
    print()
    print_status_message("Generating final report...", "info")
    report_path = generate_final_report(stats, script_dir)
    
    # Show final summary
    show_final_summary(stats, report_path)
    
    # Footer
    print()
    print(Colors.colored("=" * 80, Colors.CYAN))
    print()
    
    # Keep window open
    print(Colors.colored("Press Enter to exit...", Colors.GRAY))
    try:
        input()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print()
        print(Colors.colored("Pipeline execution interrupted by user.", Colors.YELLOW))
        sys.exit(1)
    except Exception as e:
        print()
        print(Colors.colored(f"Unexpected error: {str(e)}", Colors.RED))
        import traceback
        traceback.print_exc()
        sys.exit(1)
