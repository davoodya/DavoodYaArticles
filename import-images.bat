echo ==============: Step 1 :==============
echo ===== Import New Articles Images =====
echo ======================================
python "H:\Repo\Hugo\davoodya\convert_images.py"
echo.

echo ==============: Step 2 :==============
echo ===== Add Title for new Articles =====
echo ======================================
python "H:\Repo\Hugo\davoodya\title-adder.py"
echo.

echo ==================: Step 3 :==================
echo ===== Add ALT for Images in All Articles =====
echo ==============================================
python "H:\Repo\Hugo\davoodya\altimage-adder.py"
echo.

echo ====================: Step 4 :====================
echo ===== Rename all Images in  /static/images/* =====
echo ==================================================
python "H:\Repo\Hugo\davoodya\images-renamer.py"
echo.

echo ==================: Step 5 :==================
echo ===== Rename all Images Used in Articles =====
echo ==============================================
python "H:\Repo\Hugo\davoodya\image-article-renamer.py"
echo.

echo ====================: Step 6 :====================
echo ===== Remove Obsidians TOC from all articles =====
echo ==================================================
python "H:\Repo\Hugo\davoodya\toc-remover.py"
echo.

echo =========================: Step 7 :=========================
echo ===== Add Hugo Front Matter Properties to All Articles =====
echo ============================================================
python "H:\Repo\Hugo\davoodya\obsidian-property-remover-enhanced.py"
echo.


echo ==============================
echo ===== Execution Finished =====
echo ==============================
echo.
echo.
echo =====================================
echo ======== Start Reporting ============
echo =====================================
echo.
echo "1. New Articles Image Imported Succesfully from Obsidian Vault Attachment"
echo.
echo "2. Add new title for all new articles based on Hugo Front Matter syntax, title filled based on file name"
echo.
echo "Note: Step 2 Required for step 3 and step 4 - image renaming"
echo.
echo "3. Add ALT Value for all new imported images based on title property"
echo.
echo "4. Rename all new imported images in statc/images/category-name/*, new name based on File Name"
echo.
echo "5. Rename all new imported images Usages in the Markdown file based on new image name from step 4"
echo.
echo "6. Remove All Obsidian Table of Contents"
echo.
echo "7. Add All important front matter properties to new articles"
echo.
echo.
echo ======================================
echo ======== Finish Reporting ============
echo ======================================