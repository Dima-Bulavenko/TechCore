# TechCore (Milestone Project 5)

![Responsive Mockup](docs/responsice_dispaly.png)

## Table of contents

- [Purpose](#purpose)
- [E-commerce Business Model](#e-commerce-business-model)
- [UX Design](#ux-design)
- [Epics](#epics)
- [User Stories](#user-stories)
- [Wireframes](#wireframes)
  * [Product List page](#product-list-page)
  * [Profile page](#profile-page)
  * [Form page](#form-page)
- [Marketing Strategy](#marketing-strategy)
  * [Social Media Presence](#social-media-presence)
  * [Search Engine Optimization (SEO)](#search-engine-optimization--seo-)
- [Agile Development](#agile-development)
  * [Task Management](#task-management)
  * [Project Management](#project-management)
  * [Workflow](#workflow)
- [Design](#design)
  * [Color Scheme](#color-scheme)
  * [Typography](#typography)
- [Features](#features)
  * [User Registration and Authentication](#user-registration-and-authentication)
  * [User Profile and Notifications](#user-profile-and-notifications)
  * [Product Browsing and Filtering](#product-browsing-and-filtering)
  * [Shopping Cart and Checkout](#shopping-cart-and-checkout)
  * [Admin Management](#admin-management)
- [Database Schema](#database-schema)
- [Testing](#testing)
  * [Manual Testing](#manual-testing)
    + [Navbar](#navbar)
    + [Footer](#footer)
    + [Product List page](#product-list-page-1)
    + [Contact Us page](#contact-us-page)
    + [Cart page](#cart-page)
    + [Checkout page](#checkout-page)
    + [Payment processing](#payment-processing)
    + [Profile page](#profile-page-1)
    + [Forms](#forms)
  * [Unit testing](#unit-testing)
    + [Python unit tests](#python-unit-tests)
  * [Code validation](#code-validation)
    + [HTML Validation](#html-validation)
    + [CSS Validation](#css-validation)
    + [Python Validation](#python-validation)
    + [JS Validation](#js-validation)
  * [Lighthouse](#lighthouse)
- [Technologies](#technologies)
  * [Languages](#languages)
  * [Programs, frameworks, libraries](#programs--frameworks--libraries)
- [Environment Variables](#environment-variables)
- [Deployment](#deployment)
  * [Heroku](#heroku)
  * [Clone GitHub Repo](#clone-github-repo)
- [Bugs](#bugs)
- [Credits](#credits)
  * [Media](#media)
  * [Design Template](#design-template)
  * [Code](#code)
  * [Acknowledgements](#acknowledgements)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# Purpose

[TechCore](https://techcore-e370dc0903ef.herokuapp.com/) is an e-commerce platform built with the Django framework, designed to provide a seamless shopping experience for tech enthusiasts looking for high-performance CPUs and GPUs. Leveraging Django's powerful backend capabilities, the application features user authentication, efficient data management, and precise routing for a smooth and secure shopping journey. The frontend is enriched with Django’s templating system and HTMX for interactive and dynamic content updates, reducing page reloads and improving responsiveness.

Key features include a customizable price range filter, easy product browsing, a streamlined checkout process with Stripe integration, and a flexible cart system. These features are crafted to deliver a user-friendly and efficient shopping experience, catering to both casual tech shoppers and performance-focused enthusiasts.

[Table of contents](#table-of-contents)

# E-commerce Business Model
TechCore operates under a direct-to-consumer e-commerce model, specializing in selling high-performance CPUs and GPUs directly to customers without intermediaries. This model allows TechCore to maintain control over product selection, customer relationships, and service quality. Here’s how this business model aligns with TechCore's goals:

Key Components

- **Product Offering**: A curated selection of CPUs and GPUs, chosen to meet the needs of gamers, PC builders, and professionals seeking high-quality components.
- **Customer Segmentation**: Targeting tech enthusiasts and performance-oriented users, with a user-friendly site that facilitates easy browsing, filtering, and purchasing.
- **Revenue Streams**: Direct sales from the website, with Stripe integrated to offer a secure and seamless payment experience.
- **Marketing and Sales Channels**: Focused on multi-channel marketing, including SEO and social media, to reach a broader audience and drive traffic directly to the site.

By adopting this business model, TechCore not only aims to facilitate component sales but also seeks to build a trusted community for those passionate about high-performance hardware, providing an all-inclusive and reliable shopping experience.

# UX Design

-   **PC Builders and Gamers**: Individuals who are building or upgrading custom PCs, especially gamers seeking high-performance components. TechCore offers a curated selection of CPUs and GPUs to meet their specific needs.

-   **Tech Enthusiasts and Professionals**: Users interested in the latest advancements in computer hardware, including programmers, designers, and engineers who need powerful processors and graphics cards for intensive tasks.

-   **Retail and Wholesale Buyers**: Businesses or individual buyers looking for reliable sources for bulk or retail purchases of CPUs and GPUs, with streamlined shopping features and flexible order quantities.

-   **Price-Conscious Shoppers**: Users looking to find the best hardware within their budget range. TechCore’s price range filter allows them to explore options tailored to their budget.

# Epics

To manage the development of key features for TechCore, I organize epics on GitHub by creating issues tagged with the "Epic" label. Each epic contains a well-structured list of user stories and developer tasks that outline the required steps for feature implementation and testing.

These epics ensure that the core functionalities, such as user authentication, shopping cart operations, price filtering, and payment processing, are developed in a systematic and organized manner.

You can find all the epics [here](https://github.com/Dima-Bulavenko/TechCore/issues?q=is%3Aissue+label%3AEpic).

# User Stories

-   **User stories:** To outline the features of TechCore, I used [user stories](https://github.com/Dima-Bulavenko/TechCore/issues?q=is%3Aissue+label%3A%22User+story%22). These stories help clarify the user’s needs and expectations, such as filtering products by price, managing the shopping cart, and completing a secure checkout process. Each story is designed to focus on the user’s interaction with the platform and the desired outcomes of each feature.

[Back to the top](#table-of-contents)

# Wireframes

## Product List page

-   <details>
      <summary>Mobile</summary>
      <img src="./docs/home_mobile_wf.png"
      alt="Mobile wire frame">
    </details>

-   <details>
      <summary>Laptop</summary>
      <img src="./docs/home_laptop_wf.png">
      alt="Laptop wire frame">
    </details>

## Profile page

-   <details>
      <summary>Mobile</summary>
      <img src="./docs/profile_mobile_wf.png"
      alt="Mobile wire frame">
    </details>

-   <details>
      <summary>Laptop</summary>
      <img src="./docs/profile_laptop_wf.png">
      alt="Laptop wire frame">
    </details>

## Form page

-   <details>
      <summary>Mobile</summary>
      <img src="./docs/form_mobile_wf.png"
      alt="Mobile wire frame">
    </details>

-   <details>
      <summary>Laptop</summary>
      <img src="./docs/form_laptop_wf.png">
      alt="Laptop wire frame">
    </details>

[Back to the Top](#help-u-website-milestone-project-4)

# Marketing Strategy

The marketing strategy for TechCore focuses on building a strong online presence, attracting tech-savvy customers, and increasing sales through various digital channels. This approach includes social media engagement, search engine optimization (SEO).

## Social Media Presence

To connect with technology enthusiasts and promote the latest CPU and GPU offerings, TechCore has established a presence on [Facebook](https://www.facebook.com/profile.php?id=61567371643508) platform.
![Facebook](docs/facebook.png)

## Search Engine Optimization (SEO)

To enhance TechCore’s visibility on search engines and draw in more organic traffic, the following SEO practices are implemented:

-   [**robots.txt**](https://techcore-e370dc0903ef.herokuapp.com/robots.txt): Configured to guide web crawlers, ensuring that important pages are indexed properly and appear in search results.

-   [**Sitemap**](https://techcore-e370dc0903ef.herokuapp.com/sitemap.xml): A sitemap was created to help search engines navigate and index all TechCore’s pages, improving overall discoverability.

-   **Meta Descriptions**: Compelling meta descriptions are written for each page, improving click-through rates by providing a concise and attractive preview on search engine results pages (SERPs).

# Agile Development

In this project, I use Agile methodology to manage and track development tasks. Here's a breakdown of how I apply Agile practices:

## Task Management

-   **Issues**: Each task is represented by an issue in our GitHub repository.
-   **Labels**: Issues are categorized using labels to indicate their priority and importance:
    -   `Could Have`
    -   `Must Have`
    -   `Should Have`
    -   `Would Have`
-   **Milestones**:
    -   **Product Backlog**: This milestone includes all issues that have been identified but not yet assigned to a specific iteration. Issues in this milestone do not have time constraints.
    -   **Iteration #number**: Each iteration has a specific duration (one week) and is assigned to a milestone. Issues are moved to this milestone as they are scheduled for the current iteration.

## Project Management

-   **GitHub Kanban Board**: We use a GitHub Kanban board to represent the current iteration's state and to track progress. Each iteration has its own project board.
-   **Iteration Planning**: For each new iteration, a new project board is created. Each iteration consists of a specific number of issues that are planned for completion within the week.

## Workflow

1. **New Issues**: All new issues are added to the `Product Backlog` milestone by default.
2. **Iteration Setup**: When a new iteration begins, a new project board is created, and issues from the `Product Backlog` are selected and moved to the corresponding `Iteration #number` milestone.
3. **Execution**: During the iteration, the team works on issues as per the priority labels and tracks progress on the GitHub Kanban board.
4. **Review**: At the end of each iteration, completed issues are reviewed, and a new iteration is planned with updated priorities and tasks.

This structured approach ensures clear task prioritization and efficient tracking of progress throughout the development cycle.

# Design

## Color Scheme

The color scheme for TechCore is based on Flowbite’s components, which were adjusted to complement the modern, tech-focused design of the site. This scheme aims to create a visually appealing and professional look, enhancing the shopping experience for tech enthusiasts.

![Color Scheme](docs/techcore_color_shceme.png)

## Typography

This project uses the following Google Font:

-   [Inter](https://fonts.google.com/specimen/Inter) - for all text content.

[Back to the top](#table-of-contents)

# Features

## User Registration and Authentication

This project utilizes the Django allauth library to handle user registration, authentication, and account management, including social account integration.

-   **Registration and Authentication with Social Accounts**: Allows users to sign up and log in using social accounts.
-   **User Registration**: Enables new users to create an account with their details.
-   **User Login**: Provides users with the ability to log in using their credentials.
-   **User Logout**: Allows users to log out from their accounts.
-   **Reset Password**: Facilitates the process for users to reset their forgotten passwords.
-   **Change Password**: Allows users to change their account passwords.
-   **Set Password**: Allows users to set a password for their account if they sign up with their social account.
-   **Email Confirmation**: Sends a confirmation link to the user's email to verify that the email address belongs to the user.
-   **User Account Deletion**: Allows users to permanently delete their accounts.
-   **Admin Model Registration**: Registers models in the Django Admin interface for administrative purposes.

## User Profile and Notifications

-   **User Profile**: Provides users with a profile page where they can view and update their personal information, check list of his orders and manage account settings (password rest, Logout, Delete Account).
-   **Success and Error Toast Notifications**: Displays toast messages to inform users of success or errors during interactions.

## Product Browsing and Filtering

TechCore provides a seamless shopping experience with browsing and filtering options to help users find the right products.

-   **Browse Products**: Users can explore a variety of CPUs and GPUs.
-   **Price Range Filter**: Allows users to filter products based on their budget preferences.
-   **Product Details Page**: Displays detailed information about each product, including specifications and pricing.

## Shopping Cart and Checkout

The shopping cart and checkout system are designed to make purchasing as straightforward as possible.

-   **Add to Cart**: Users can add items to their cart with ease.
-   **Adjust Quantity in Cart**: Users can increase or decrease the quantity of items.
-   **Remove Item from Cart**: Enables users to remove specific items from the cart.
-   **Proceed to Checkout**: Streamlines the checkout process.
-   **Stripe Payment Integration**: Provides a secure and reliable payment method through Stripe.
-   **Order Summary**: Displays a summary of the order before completing the purchase.

## Admin Management

The admin panel helps administrators manage customer orders efficiently.

-   **Product and Order Management**: Admins can add, update, and remove products and manage user orders.

# Database Schema

The database schema for TechCore is structured to support both product management and user interactions.

![Database Schema](docs/db_schema.png)

[Back to the top](#table-of-contents)

# Testing

## Manual Testing

### Navbar

-   :heavy_check_mark: Navbar layout displays correctly on different screen sizes.
-   :heavy_check_mark: All links are working correctly.
-   :heavy_check_mark: The burger menu functions correctly on mobile devices.
-   :heavy_check_mark: Anonymous users do not see links that are only for authenticated users.
-   :heavy_check_mark: **Cart icon is updated** items amount.
-   :heavy_check_mark: **Product Search input** work correctly.
-   :heavy_check_mark: **User profile button** work correctly.

### Footer

-   :heavy_check_mark: Footer layout displays correctly on different screen sizes.
-   :heavy_check_mark: All links are working correctly.
-   :heavy_check_mark: The link to the GitHub repo opens in a new tab.
-   :heavy_check_mark: The link to the Facebook page opens in a new tab.
-   :heavy_check_mark: Email subscription works correctly.

### Product List page

-   :heavy_check_mark: **Add to cart** button works correctly.
-   :heavy_check_mark: **Links to product detail** works correctly.
-   :heavy_check_mark: **Filler product form** detail works correctly.
-   :heavy_check_mark: **Clear filter** buttons works correctly.
-   :heavy_check_mark: **Product rating stars** show correct information.
-   :heavy_check_mark: **Product pagination** works correctly.
-   :heavy_check_mark: **Product ordering** works correctly.

### Contact Us page

-   :heavy_check_mark: **Form** works correctly.
-   :heavy_check_mark: **Form prefilled** with user email.

### Cart page

-   :heavy_check_mark: **Remove item** buttons work correctly.
-   :heavy_check_mark: **Change item quantity** buttons work correctly.
-   :heavy_check_mark: **Checkout and continue shopping** buttons work correctly.
-   :heavy_check_mark: **Order Summary Calculation** works correctly.

### Checkout page

-   :heavy_check_mark: **Form** works correctly.
-   :heavy_check_mark: **Form prefilled** with user data.
-   :heavy_check_mark: **Payment form** works correctly.
-   :heavy_check_mark: **Order Summary Calculation** works correctly.
-   :heavy_check_mark: **Forms validation** works correctly.
-   :heavy_check_mark: **Order items list** is displayed correctly.
-   :heavy_check_mark: **Adjust Cart button** works correctly.
-   :heavy_check_mark: **Complete Order button** works correctly.
-   :heavy_check_mark: **Processing order backdrop** works correctly.

### Payment processing

-   :heavy_check_mark: **Payment success** works correctly.
-   :heavy_check_mark: **Payment failure** works correctly.
-   :heavy_check_mark: **Payment success email** is sended.
-   :heavy_check_mark: **Payment with authentication success** works correctly.
-   :heavy_check_mark: **Payment with authentication fail** works correctly.

### Profile page

-   For anonymous users:

    -   :heavy_check_mark: Get redirect to the welcome page.

-   For authenticated users:
    -   :heavy_check_mark: All links are working correctly.
    -   :heavy_check_mark: User can change the password.
    -   :heavy_check_mark: User can delete the account.
    -   :heavy_check_mark: User can set/update shipping address.
    -   :heavy_check_mark: User can set/update his details.
    -   :heavy_check_mark: User can seen general information about his account.
    -   :heavy_check_mark: User can see list of his orders.

### Forms

-   :heavy_check_mark: All forms are displayed correctly.
-   :heavy_check_mark: All form fields and buttons work correctly.

[Back to the top](#table-of-contents)

## Unit testing

### Python unit tests

Unit tests was create with django built-in django test functionality. To run the tests, run the following command in the terminal:

```bash
python manage.py test
```

<details>
  <summary>Test results:</summary>
  <img src="./docs/python_tests.png" alt="Python unit tests">
</details>

## Code validation

### HTML Validation

To validate the HTML code, I use the [W3C HTML Markup Validator](https://validator.w3.org/#validate_by_uri). Since I use htmx in my project, the validator will show some errors related to the htmx attributes, but these can be ignored.

-   :heavy_check_mark: [Product list page](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftechcore-e370dc0903ef.herokuapp.com%2Fproduct%2FCPU#cl3200c20)

-   :heavy_check_mark: [Contact Us page](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftechcore-e370dc0903ef.herokuapp.com%2Fcontact-us%2F#cl3200c20)

-   :heavy_check_mark: [Authentication pages](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftechcore-e370dc0903ef.herokuapp.com%2Faccounts%2Flogin%2F#cl3200c20)

-   :heavy_check_mark: [Authentication pages](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftechcore-e370dc0903ef.herokuapp.com%2Faccounts%2Flogin%2F#cl3200c20)

-   <details>
       <summary>Cart page</summary>
       <img src="./docs/html_validator_cart_page.png"
       alt="Cart page">
     </details>

-   <details>
       <summary>Checkout page</summary>
       <img src="./docs/html_validator.checkout_page.png"
       alt="Checkout page">
     </details>

-   <details>
       <summary>Profile page</summary>
       <img src="./docs/html_validator_profile_page.png"
       alt="Profile page">
     </details>

### CSS Validation

To validate the CSS code, I use the [W3 Jigsaw validator](https://jigsaw.w3.org/css-validator/#validate_by_uri).

-   :heavy_check_mark: [dist/style.css](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Ftechcore-e370dc0903ef.herokuapp.com%2Fproduct%2FCPU&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en). I was used tailwind css to create styles, so the validator shows some errors related to the tailwind classes, but these can be ignored.

### Python Validation

To validate the Python code I use [Ruff](https://docs.astral.sh/ruff/) VScode extension.

-   :heavy_check_mark: No errors found.

### JS Validation

To validate the JS code I use [ESLint] VScode extension(https://eslint.org/).

-   :heavy_check_mark: No errors found.

[Back to the top](#table-of-contents)

## Lighthouse

-   :heavy_check_mark: [Product list page](https://pagespeed.web.dev/analysis/https-techcore-e370dc0903ef-herokuapp-com-product-CPU/yuvwsu6laa?form_factor=mobile)

-   :heavy_check_mark: [Cart page](https://pagespeed.web.dev/analysis/https-techcore-e370dc0903ef-herokuapp-com-cart/kyj2thz1ul?form_factor=mobile)

-   :heavy_check_mark: [Contact Us](https://pagespeed.web.dev/analysis/https-techcore-e370dc0903ef-herokuapp-com-contact-us/tocmkwpb38?form_factor=mobile)

-   :heavy_check_mark: [Authentication pages](https://pagespeed.web.dev/analysis/https-techcore-e370dc0903ef-herokuapp-com-accounts-signup/jbuq2wn4dh?form_factor=mobile)

[Back to the top](#table-of-contents)

# Technologies

## Languages

-   Python+Django, JavaScript, HTML, CSS, Tailwind CSS.

## Programs, frameworks, libraries

-   [Django](https://www.djangoproject.com/) for backend and frontend functionality.
-   [PostgreSQL](https://www.postgresql.org/) relational database.
-   [Psycopg](https://www.psycopg.org/) PostgreSQL adapter for Python.
-   [Google Fonts](https://fonts.google.com/) for typography.
-   [GitHub](https://GitHub.com/) to host the source code.
-   [Heroku](https://www.heroku.com/) to deploy and host the live app.
-   [Unittest](https://docs.python.org/3/library/unittest.html) for Python unit-testing.
-   [W3C HTML Markup Validator](https://validator.w3.org/) to validate HTML code.
-   [W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) to validate CSS code.
-   [django-allauth](https://docs.allauth.org/en/latest/introduction/index.html) - help to set up social authentication.
-   [dj-database-url](https://github.com/jazzband/dj-database-url/) - allows to use URLs to connect to DB
-   [js-cookie](https://github.com/js-cookie/js-cookie/) - JavaScript API for handling cookies
-   [django-htmx](https://django-htmx.readthedocs.io/en/latest/index.html) - make using htmx in Django easier.
-   [django-tailwind](https://pypi.org/project/django-tailwind/) - helps to use tailwind css in Django.
-   [htmx](https://htmx.org/) - helps to create dynamic and interactive web pages.
-   [stripe](https://stripe.com/docs) - payment processing.
-   [tailwindcss](https://tailwindcss.com/) - utility-first CSS framework.
-   [flowbite](https://flowbite.com/) - HTML, CSS, and JS components.

[Back to the top](#table-of-contents)

# Environment Variables

To run this project locally, you will need to create a `.env` file in the root directory of the project and add the following environment variables:

```bash
DJANGO_SETTINGS_MODULE=tech_core.settings.dev

SECRET_KEY=
DEBUG=True

# STRIPE
STRIPE_PUBLIC_KEY=
STRIPE_SECRET_KEY=
STRIPE_WH_SECRET=

DB_TYPE=sqlite3
DATABASE_URL=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
FACEBOOK_CLIENT_ID=
FACEBOOK_CLIENT_SECRET=

# AWS
AWS_SECRET_ACCESS_KEY=
AWS_ACCESS_KEY_ID=
AWS_STORAGE_BUCKET_NAME=
AWS_S3_REGION_NAME=
```

`GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, FACEBOOK_CLIENT_ID, FACEBOOK_CLIENT_SECRET` used for user social authentication.

# Deployment

## Heroku

The TechCore project was deployed on a Heroku hosting server. The following steps outline the process of deploying the TechCore project and can be applied to deploy another Django project with minor adjustments:

1.  Navigate to your [Heroku dashboard](https://dashboard.heroku.com/apps) and create a new app with a unique name.

2.  Navigate to **Settings** in [Heroku dashboard](https://dashboard.heroku.com/apps) and click **Add buildpacks** and choose "nodejs". This buildpack is required to be at te top of the buildpack list.

3.  Install `gunicorn` as a production-ready webserver for Heroku with command.

    ```
    pip install gunicorn
    ```

4.  Create a file named `Procfile` at the root directory of the project.

5.  Add following command to `Procfile` to run your server in production.

    ```
    web: gunicorn tech_core.wsgi
    ```

    <sub>**Note**: Replace `tech_core` with your project name</sub>

6.  In the `settings.py` file update the `ALLOWED_HOSTS` variable.

    ```python
    ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']
    ```

7.  Install [dj-database-url](https://pypi.org/project/dj-database-url/).

    ```
    pip install dj-database-url
    ```

8.  Import `dj-database-url` in `settings.py`.

    ```python
    import dj_database_url
    ```

9.  Install [psycopg3](https://pypi.org/project/psycopg/) to connect to PostgreSQL database.

    ```
    pip install "psycopg[binary,pool]"
    ```

10. In the `settings.py` replace `DATABASES` with the following code:

    ```python
    if DEBUG:
        DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": config("DB_NAME"),
            "USER": config("DB_USER"),
            "PASSWORD": config("DB_PASSWORD"),
            "HOST": config("DB_HOST"),
            "PORT": config("DB_PORT"),
            }
        }
    else:
        DATABASES = {
            'default': dj_database_url.parse(config('DATABASE_URL'))
        }
    ```

    <sub>**Note**: Replace `if` clause with your own database for local development</sub>

11. In the `.env` file update the `DEBUG` environment variable and add `DATABASE_URL` new one.

    ```
    DEBUG=False
    DATABASE_URL=add_URL_of_a_remote_database
    ```

    <sub>**Note**: For the TechCore I used database URL provided by `Code Institute` but you can use other database hosting services< such as [Amazon RDS for PostgreSQL](https://aws.amazon.com/rds/postgresql/)/sub>

12. **Reload your terminal** and run the following command in **terminal** to migrate remote database.

    ```
    python manage.py migrate
    ```

13. Replace `DEBUG=False` to `DEBUG=True` in the `.env` file.

14. Return to the [Heroku dashboard](https://dashboard.heroku.com/) navigate to the **Settings** tab and click on **Reveal Config Var** and add `DATABASE_URL` environment variable.

15. Install [whitenoise](https://pypi.org/project/whitenoise/) to manage static files on production server.

    ```
    pip install whitenoise
    ```

16. Add `whitenoise` to the `MIDDLEWARE` list in the `settings.py`.

    ```python
    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        'whitenoise.middleware.WhiteNoiseMiddleware',
    ]
    ```

    <sub>**Note**: The WhiteNoise middleware must be placed directly after the Django `SecurityMiddleware`</sub>

17. Add `STATIC_ROOT` and `STORAGES` variables to the `settings.py`.

    ```python
    STORAGES = {
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        },
    }
    STATIC_ROOT = BASE_DIR.joinpath("staticfiles")
    ```

18. Run the following command in **terminal** to collect static files.

    ```
    python manage.py tailwind build
    python manage.py collectstatic
    ```

19. From the terminal, check the Python version used in your IDE.

    ```
    python --version
    ```

20. Look up the [supported runtimes here](https://devcenter.heroku.com/articles/python-support#specifying-a-python-version) and copy the runtime closest to the one used in your IDE.

21. Add a `runtime.txt` file to your app's root directory.

22. Paste the copied runtime into the `runtime.txt` file.

23. Update `requirements.txt`.

    ```
    pip freeze > requirements.txt
    ```

24. Add and commit all changes to the repository.

    ```
    git add .
    git commit -m "Deploying to Heroku"
    ```

25. Push the changes to your remote branch that you intend to deploy.

    ```
    git push
    ```

26. On the [Heroku dashboard](https://dashboard.heroku.com/apps), and in your app, click on the **Deploy** tab.

27. In the **Deployment method** section enable GitHub integration by clicking on **Connect to GitHub**.

28. Start typing your project repo name into the search box and click **Search**. A list of repositories from your GitHub account should appear. Click on the GitHub repo you want to deploy from.

29. Scroll to the bottom of the page in the **Manual deploy** section, choose branch you want to deploy and click **Deploy Branch** to start a manual deployment of the branch.

30. Open the **Resources** tab and choose an eco dyno. This dyno is a lightweight container to run your project.

31. Verify there is no existing Postgres database **add-on**. if there is a database add-on select **Delete Add-on** to remove it.

32. Click on **Open app** to view your deployed project.

[Back to the top](#table-of-contents)

## Clone GitHub Repo

1.  Log into your account on GitHub
2.  Go to the repository of this project [TechCore](https://github.com/Dima-Bulavenko/TechCore)
3.  Click on the **code** button, and copy your preferred clone link.
4.  Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5.  Type `git clone` into the terminal, paste the link you copied in step 3 and press enter.

[Back to the top](#table-of-contents)

# Bugs

-   All fixed bugs can be found [here](https://github.com/Dima-Bulavenko/TechCore/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

-   All unfixed bugs can be found [here](https://github.com/Dima-Bulavenko/TechCore/issues?q=is%3Aissue+label%3Abug+is%3Aopen)

[Back to top](#contents)

# Credits

## Media

-   icons from [Font Awesome](https://fontawesome.com/)

[Back to the top](#table-of-contents)

## Design Template

-   [Animated burger menu](https://codepen.io/ainalem/pen/GeMqdP)

-   [Layout of shopping cart page](https://flowbite.com/blocks/e-commerce/shopping-cart/)

[Back to the top](#table-of-contents)

## Code

-   [Implementing infinite scroll in Django with htmx](https://medium.com/@franciscovcbm/infinite-scroll-with-django-and-htmx-27f61cfaf911)

-   [Dynamic messages with HTMX and Alpine.js](https://danjacob.net/posts/htmx_messages/)

-   [django-tailwind build on heroku](https://medium.com/@phuitsing/heroku-buildpack-for-django-tailwind-de96be543f9)

[Back to the top](#table-of-contents)

## Acknowledgements

I want to convey my immense gratitude to my mentor, [Luke Buchanan](https://www.linkedin.com/in/lukebuchanan67/), for pinpointing my mistakes and providing advice on how to rectify them. Special thanks to my friends who assisted in testing the application, and to the Slack community, always ready to offer valuable tips at any time.

[Back to the top](#table-of-contents)
