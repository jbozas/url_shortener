### URL Shortener Service ###

# Overview
Tool that take long URLs and create shorter, more manageable versions. These shortened URLs, composed of a random sequence of characters, redirect users to the original, longer URL when clicked.

Workflow
1. User Input
Users provide the long URL they wish to shorten. This URL could point to various online resources such as webpages, images, documents, or any other accessible content.

1. Shortening Algorithm
The URL shortener service employs a shortening algorithm to generate a unique short code or identifier for the given URL. This short code becomes an integral part of the shortened URL.

1. Database Entry
The original long URL and its corresponding short code are stored in a database. This database entry facilitates the mapping of the short code back to the original URL when users access the shortened link.

1. Creation of Shortened URL
The service combines its domain with the generated short code to create the final shortened URL. For instance, if the service's domain is "short.url" and the short code is "abc123," the resulting shortened URL would be "https://short.url/abc123."

1. Redirection
When users click on the shortened URL, the service receives the request and looks up the short code in its database. If a match is found, the service redirects the user to the original long URL associated with that short code.

1. Analytics and Tracking (ToDo)
Some URL shortener services offer optional analytics and tracking features. These can include metrics such as the number of clicks, geographic locations of users, referral sources, and more. This data proves valuable for link creators to assess the performance of their shortened links.

# Purposes of this service

* User-Friendly Links: make long URLs more user-friendly, especially in contexts where character count is limited, such as on platforms like Twitter.
* Space-saving
* Analytics and Tracking: provide valuable insights through analytics and tracking features, aiding in understanding link performance.



# Deployment

* Without Docker:
```
python asgi.py
```
