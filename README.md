# Scraping Wikipedia - I: Scraping the page names from Wikipedia category hierarchy

<p align='center'>
<img src="https://github.com/SwamiKannan/Scraping_Wikipedia_categories/blob/main/images/category_scrapes.png">
</p>


This git is specially for the purpose of populating a list of pages / categories that can be entered into Wikipedia's [Special Export](https://en.wikipedia.org/wiki/Special:Export) page to request XML files. 

I was in the process of creating an AI assistant for Physics and was trying to download the requisite information from Wikipedia for this purpose. Wikipedia allows us to:
<ol>
  <li> Download all article for a single category say Physics from their <a href="https://en.wikipedia.org/wiki/Special:Export">Special:Export page.</a></li>
  <li> Download an unrelated bunch of pages in a single XML format from their <a href="https://en.wikipedia.org/wiki/Special:Export">Special:Export page.</a></li>
  <li> Download the <a href="https://en.wikipedia.org/wiki/Special:Export/Train"> XML file </a>for the current revision of a single article.</li>
  <li> Just <a href="https://dumps.wikimedia.org/"> download the entire Wikipedia database </a> and parse the entire Wikipedia database.</li>
</ol>
However, I needed, not just the articles that come under the  "Physics" category, but also the articles that come under the subcategories of Physics e.g. the pages under <a href='https://en.wikipedia.org/wiki/Category:Astrophysics'><i>Astrophysics</i></a> or <a href='https://en.wikipedia.org/wiki/Category:Physicists_by_nationality'><i>Physicists by nationality</i></a>, etc. Parsing the whole database and then filtering out the various categories I wanted was troublesome. Hence, this git.


<br>

## How to run the library
### 1. Download the git file
```
git clone https://github.com/SwamiKannan/Scraping_Wikipedia_categories.git
```

### 2. Pip install the requirements
Through the command window, navigate to the git folder and run:
```
pip install -r requirements.txt
```
#### Note 1: This assumes that you have already python, and the pip and git libraries installed.
### 3. Decide your parameters
1. Get the URL from where you want to scrape the subcategories and pages. This URL must be a **category** page in Wikipedia i.e. URL of the format: **https://en.wikipedia.org/wiki/Category:**
2. Decide on the maximum number of sub-categories you would like to scrape (optional)
3. Decide on the maximum number of page names you would like to extract (optional)
4. Decide on the depth of the category tree that you would like to extract the page names for (depth is explained in the cover image above)

#### Note 2: If you provide (2), (3) and (4), which ever criteria is met first will halt the scraping
#### Note 3: If you do not provide (2) or (3) or (4) above, the script will keep running until all subcategories are exhausted. This is not recommended since within 7 levels of depth, you can go from Physics to Selena Gomez' We Own the Night Tour page as below:
   <p align = "center">
   <img src="https://github.com/SwamiKannan/Scraping_Wikipedia_categories/blob/main/images/depth_gone_wrong.png">
   </p>
   
### 4. Run the code below:
First navigate to the 'src' directory.
Then run the code below:
```
python get_pages.py "<source category page>" -o <output_directory> (optional) -pl <max number of pages to be downloaded> -cl<max number of categories to be downloaded> -d <depth of scraping>
```

## Outputs:
A folder "data" in the chosen output directory (or in the root directory of the repository if no output directory provided)
<ol>
  <li>category_names.txt  - A text file containing the list of categories / sub-categories that have been identified</li>
  <li>category_links.txt  - A text file containing the list of categories / sub-categories **urls** that have been identified</li>
  <li>page_names.txt  - A text file containing the list of pages that have been populated</li>
  <li>page_links.txt  - A text file containing the list of page **urls** that have been populated</li>
  <li>done_links.txt - A text file containing the list of categories that have been identified **and traversed**. This is a reference only if we want to restart the session with the same parent Category.</li>
</ol>

## Usage:
### Option 1: Through the browser
1a. Go to <a href="https://en.wikipedia.org/wiki/Special:Export"> the Wikipedia's Export page </a> <br />
1b. Enter the details from category_names.txt or page_names.txt as below:
<p align='center'>
  <img src="https://github.com/SwamiKannan/Scraping_Wikipedia_Category-Hierarchy/blob/main/images/usage.png"
</p>
  
OR
### Option 2: Through Python
2a. Run the following code:
```
  pip install requests
```
2b. Inside a python console, type the following code:
  ```
  import requests

  page_name = "<insert any page name from page_names.txt>"

  url='https://en.wikipedia.org/wiki/Special:Export/'+page_name

  response=requests.get(url)
  if response.status_code==200:
    content= response.content

  if content:
    with open(<choose a filename ending with .xml>,'w',encoding='utf-8') as outfile:
      outfile.write(content)
```
