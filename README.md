## Usage

To use the `rapi` library to fetch information about a subreddit and its top post, follow these instructions:

1. Import the `rapi` library in your Python script:

    ```python
    import rapi
    ```

2. Use the `get_subreddit` function to retrieve information about a subreddit and its top post. Customize the function parameters based on your requirements:

    ```python
    get_subreddit(subreddit="memes", limit=10, type="title", username=True, post_link=True, comments=False)
    ```

    - `subreddit`: Replace "memes" with the subreddit you want to fetch information from.
    - `limit`: Specify the number of posts to retrieve (default is 10).
    - `type`: Specify the type of information to retrieve (e.g., "title", "json", "text").
    - `sort`: Specify the sorting method for posts ("hot", "new", "top", "rising").
    - `username`: Set to `True` if you want to include the username in the output.
    - `post_link`: Set to `True` if you want to include the post link in the output.
    - `comments`: Set to `True` if you want to include comments in the output.


3. Customize the output based on your needs and integrate it into your project.

## Example

Here's an example of how to use the `get_subreddit` function:

```python
import rapi

subreddit = get_subreddit(subreddit="memes", limit=1, type="title", username=True, post_link=True, comments=False)

print(subreddit)
```
