echo ==============================================
echo ===== Step 1: Import New Articles Images =====
echo ==============================================
python "H:\Repo\Hugo\davoodya\convert_images.py"
echo.

echo ==============================================
echo ===== Step 2: Add Title for new Articles =====
echo ==============================================
python "H:\Repo\Hugo\davoodya\title-adder.py"
echo.

echo ======================================================
echo ===== Step 3: Add ALT for Images in All Articles =====
echo ======================================================
python "H:\Repo\Hugo\davoodya\altimage-adder.py"
echo.

echo =========================================================
echo ===== Step 4: Rename all Images in /static/images/* =====
echo =========================================================
python "H:\Repo\Hugo\davoodya\images-renamer.py"
echo.

echo ======================================================
echo ===== Step 5: Rename all Images Used in Articles =====
echo ======================================================
python "H:\Repo\Hugo\davoodya\image-article-renamer.py"
echo.


echo =====================================
echo ===== Image Importing Completed =====
echo =====================================