
# The Knowledge Society

## 1. Project Goals
The purpose of this project is to create a Django Rest Framework API for The Knowledge Society Web App. The design and creation of the API takes into consideration future compatibility for native app.

The Knowledge Society book club is a web application to create an engaging platform where book lovers can share and comment their favorite books, fostering a vibrant community of avid readers. The application aims to provide a seamless and interactive experience for members to discover new books and expand their knowledge and literary horizons. By facilitating meaningful interactions and promoting a love for reading, The Knowledge Society aims to create a supportive and inclusive environment that encourages intellectual growth and fosters a lifelong passion for books.

The primary goals of the web app are to:

Design an engaging web application with interactive user interfaces using HTML, CSS, and advanced JavaScript (React), focusing on organizing components effectively and separating different concerns. For more information.

Describe the crucial role played by specialist Front-End developers in modern software development and delivery processes, highlighting their expertise in creating user-friendly and visually appealing interfaces.

Develop an Application Programming Interface (API) in the current repository that can be utilized by third-party applications, enabling seamless integration and data exchange.

Build distinct and customized models that cater to the specific needs and requirements of the application, ensuring uniqueness and efficiency in data representation.

Construct an engaging Front-End application that utilizes data from an API, allowing users to interact with and manipulate the information in an interactive and meaningful manner.

## 2. Technologies I've used
- Python was used to write the functions and models as needed by the business logic.
- Django Rest Framework was used to create the project and app’s functionality (Models, Serializers and Views).

## 3. Database Design
This is the Relational Database used to create the models for the web application. [Database schema](https://github.com/David-Angel-M/knowledge-society-api/blob/main/doc/DB_Post.jpg)

## 4. User stories
###  4.1 Home
As a site user, I want to be able to publish or update posts.

###  4.2 Create Post
As a site user, I want to be able to create a post to publish on the blog. 

###  4.3 Update Post
As a site user, I want to be able to edit a post and make changes to its fields. 

###  4.4 Delete Post
As a site user, I want to be able to delete a post so that it no longer appears on the blog. 

## 5. API Reference
[Link to the Api](https://knowledge-society-bc51a0144a7f.herokuapp.com/)

#### GET all post
```http
   https://knowledge-society-bc51a0144a7f.herokuapp.com/v1/post-list/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
|  `None`   | `Array`  | Get all post|

#### POST Create
```http
  https://knowledge-society-bc51a0144a7f.herokuapp.com/v1/post/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

{
    "title": "string",
    "description": "string",
    "user": "string",
    "category": "number"
}

#### GET Detail post
```http
  https://knowledge-society-bc51a0144a7f.herokuapp.com/v1/post/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### PUT Detail post
```http
  https://knowledge-society-bc51a0144a7f.herokuapp.com/v1/post/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

{
    "title": "string",
    "description": "string",
    "category": "number"
}

#### DELETE post
```http
  https://knowledge-society-bc51a0144a7f.herokuapp.com/v1/post-delete/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

## 6. Testing
### 6.1 API Endpoints Testing
- I verify that all API endpoints are working correctly and returning the expected responses.
- Each endpoint was tested with different HTTP methods (GET, POST, PUT, DELETE) to ensure proper functionality.
- I check the appropriate status codes (e.g., 200 OK, 201 Created, 400 Bad Request, 404 Not Found) for different scenarios.

### 6.2 Input Validation Testing
- The input validation for all API endpoints corresponding with the fields of the models

### 6.3 Data Integrity Testing
- I verify the integrity of data stored in the database by performing CRUD (Create, Read, Update, Delete) operations through the API.
- I checked that data is saved correctly, updated accurately, and deleted successfully.
- I checked that data retrieval is returned for different scenarios.

### 6.4 Cross-Origin Resource Sharing (CORS) Testing:
- I verified that the appropriate CORS headers are included in API responses.

## 7. Deployment
The site was deployed using Heroku, by following the steps found in the tutorials and guidelines of CodeInstitute’s material:

- Using my Heroku account
- Create a new app whilst logged in
- Connect my GitHub repository via "Connect to GitHub" option in Heroku
- Set up the config vars for the project.
- Enable either "Automatic Deploy"

## 8. Credits and references
- Stackoverflow.
- Student Care.
- Slack Community.
- W3Schools.
- Family and Friends.

## 9. Acknowledgements
This API was created for my PP5 Project for the Full Stack Developer program with Code Institute.
DAVID ANGEL, 2022/2023
