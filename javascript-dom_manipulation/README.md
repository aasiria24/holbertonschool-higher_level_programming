# JavaScript DOM Manipulation

A collection of JavaScript scripts that demonstrate DOM manipulation, event handling, and API requests using the Fetch API.

## Learning Objectives

- Select HTML elements using `document.querySelector`
- Understand the differences between ID, class, and tag name selectors
- Modify HTML element styles and content
- Manipulate the DOM (add, remove, update elements)
- Make HTTP requests using the Fetch API
- Listen and respond to DOM and user events

## Requirements

- All scripts are interpreted on Chrome (version 57.0 or later)
- Code is `semistandard` compliant
- `var` is not used — only `let` and `const`
- No page reloads for any action (DOM manipulation, data fetching, etc.)

## Files

| File | Description |
|------|-------------|
| `0-script.js` | Changes the text color of the `<header>` element to red (`#FF0000`) using `document.querySelector` |
| `1-script.js` | Changes the text color of the `<header>` to red when the user clicks on `#red_header` |
| `2-script.js` | Adds the CSS class `red` to the `<header>` element on click of `#red_header` |
| `3-script.js` | Toggles the `<header>` class between `red` and `green` on click of `#toggle_header` |
| `4-script.js` | Adds a new `<li>Item</li>` to `.my_list` on each click of `#add_item` |
| `5-script.js` | Updates the `<header>` text to `New Header!!!` on click of `#update_header` |
| `6-script.js` | Fetches a Star Wars character name from the SWAPI and displays it in `#character` |
| `7-script.js` | Fetches all Star Wars movie titles from the SWAPI and lists them in `#list_movies` |
| `8-script.js` | Fetches the French translation of "Hello" from an API and displays it in `#hello` (works from `<head>`) |
| `100-script.js` | Adds, removes, and clears `<li>` elements from a list on user clicks (works from `<head>`) |
| `101-script.js` | Fetches the translation of "Hello" based on a selected language code and displays it on button click (works from `<head>`) |

## Usage

Each script is linked to a corresponding HTML file. Open the HTML file in Chrome and interact with the page elements as described.

```bash
# Example: open a task in Chrome
google-chrome 0-main.html
```

## APIs Used

- [SWAPI](https://swapi-api.hbtn.io/api/) — Star Wars API for character and film data
- [Hellosalut](https://hellosalut.stefanbohacek.com/) — Multilingual "Hello" translation API

## Author

**Amaal Asiri**, Holberton School — JavaScript DOM Manipulation Project
