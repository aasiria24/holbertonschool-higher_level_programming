#!/usr/bin/env python3
"""
Module for fetching and processing posts from JSONPlaceholder API
"""

import requests
import csv
from typing import List, Dict, Any


def fetch_and_print_posts() -> None:
    """
    Fetches posts from JSONPlaceholder API and prints the status code
    and titles of all posts
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post['title'])


def fetch_and_save_posts() -> None:
    """
    Fetches posts from JSONPlaceholder API, structures the data,
    and saves it to a CSV file
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        posts = response.json()

        structured_posts = []
        for post in posts:
            structured_post = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            structured_posts.append(structured_post)

        with open('posts.csv', 'w', newline='', encoding='utf-8') as csv_file:
            fieldnames = ['id', 'title', 'body']

            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()

            writer.writerows(structured_posts)

        print(f"Data has been saved to posts.csv with {len(structured_posts)} posts")


def fetch_and_save_posts_alt() -> None:
    """
    Alternative implementation using list comprehensions
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        posts = response.json()

        structured_posts = [
            {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            for post in posts
        ]

        with open('posts.csv', 'w', newline='', encoding='utf-8') as csv_file:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(structured_posts)


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
