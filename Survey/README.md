<!-- GETTING STARTED -->
## Installation

### local

* Create venv
* clone
```sh
  git clone https://github.com/Fameless4ellL/SurveyDjango.git
```
* install 
```sh
  pip install -r requirements.txt
```
* run
```sh
  py manage.py runserver
```
### Docker
* clone
```sh
  git clone https://github.com/Fameless4ellL/SurveyDjango.git
```
* build
```sh
  docker-compose build
```
* run
```sh
  docker-compose up
```




**API**
----
  Additional information about API call.

* **URL**

  /api/polls/<_poll_id_>

* **Method:**

  `GET` | `POST` | `DELETE` | `PATCH`
  
*  **URL Params** 

   **Required:**
 
   None

   **Optional:**
 
   `id=[integer]`
   

* **Data Params**

  `id=[integer]` `title_p=[string]` `desc_p=[string]` `s_date=[date]` `e_date=[date]`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ id : 1 }`
    
  OR
  
  * **Code:** 204 <br />
  
  OR
  
  * **Code:** 201 <br />
    **Content:** `{
        "title_p": "title_p",
        "desc_p": "desc_p",
        "s_date": "%Y-%m-%d",
        "e_date": "%Y-%m-%d"
    }`
 
* **Error Response:**

  * **Code:** 400 Bad Request <br />
    **Content:** `{
    "title_p": [
        "This field is required."
    ],
    "desc_p": [
        "This field is required."
    ],
    "e_date": [
        "This field is required."
    ]
}`

  OR

  * **Code:** 404 Not Found <br />
    **Content:** `{
    "detail": "Not found."
}`

----


* **URL**

  /api/polls/questions/<_int:question_id_>

* **Method:**

  `GET` | `DELETE` | `PATCH`
  
*  **URL Params** 

   **Required:**
 
   None

   **Optional:**
 
   `id=[integer]`
   

* **Data Params**

  `id=[integer]` `descriptionQA=[string]`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ id : 1 }`
    
  OR
  
  * **Code:** 204 <br />
  
 
* **Error Response:**

  * **Code:** 404 Not Found <br />
    **Content:** `{
    "detail": "Not found."
}`

----

* **URL**

  /api/polls/questions/<_int:question_id_>/choices/

* **Method:**

  `POST` 
  
*  **URL Params** 

   **Required:**
 
   `id=[integer]`

   **Optional:**
 
   None
   

* **Data Params**

  `choice_text=[string]`

* **Success Response:**

  * **Code:** 201 <br />
    **Content:** `{ choice_text : str }`
    
  OR
  
  * **Code:** 204 <br />
  
 
* **Error Response:**

  * **Code:** 400 Bad Request <br />
    **Content:** `{
    "choice_text": [
        "This field is required."
    ]
}`

    OR
    
  * **Code:** 404 Not Found <br />

----

* **URL**

  /api/polls/questions/<_int:question_id_>/vote/

* **Method:**

  `PATCH` 
  
*  **URL Params** 

   **Required:**
 
   `id=[integer]`

   **Optional:**
 
   None
   

* **Data Params**

  `choice_id=[int]`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ choice_id : int }`
  
 
* **Error Response:**

  * **Code:** 400 Bad Request <br />
    **Content:** `{
    "choice_id": [
        "This field is required."
    ]
}`

    OR
    
  * **Code:** 404 Not Found <br />

----

* **URL**

  /api/polls/questions/<_int:question_id_>/result/

* **Method:**

  `GET` 
  
*  **URL Params** 

   **Required:**
 
   `id=[integer]`

   **Optional:**
 
   None     

* **Data Params**

   None

* **Success Response:**

  * **Code:** 200 <br />
    
* **Error Response:**
   
  * **Code:** 404 Not Found <br />
  
<p align="right">(<a href="#top">back to top</a>)</p>
