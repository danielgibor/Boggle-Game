<h1 align="center">Boggle</h1>

<div align="center">
<div align="center">

  <p align="center">
    My implementation of
    <a href="https://en.wikipedia.org/wiki/Boggle" target="_blank">Boggle game</a>
</div>

![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/navendu-pottekkat/awesome-readme?include_prereleases)
![GitHub last commit](https://img.shields.io/github/last-commit/danielgibor/Boggle-Game?color=orange)
![GitHub issues](https://img.shields.io/github/issues/danielgibor/Boggle-Game?color=yellow)
![GitHub pull requests](https://img.shields.io/github/issues-pr/danielgibor/Boggle-Game?color=yellow)
![GitHub repo size](https://img.shields.io/github/repo-size/danielgibor/Boggle-Game)
![GitHub](https://img.shields.io/github/license/danielgibor/Boggle-Game)

<a href="https://github.com/danielgibor/Boggle-Game/issues">Report Bug</a>
·
<a href="https://github.com/danielgibor/Boggle-Game/issues">Request
Feature</a>
</div>

## About the project

In this project, I am implementing the game Boggle. The game consists of a 4x4 board of dice, each die having a letter on it. At the beginning of the game, a random board with letters is generated. There is only one player, and from the moment the game starts, the player has 3 minutes to score as many points as possible by finding valid words on the board.

A valid word is defined as a word that appears in the dictionary and is formed by a path on the game board that starts at one letter and moves to adjacent letters. An adjacent letter is considered to be a letter that is next to the current letter in any of the eight directions (up, down, right, left, or any of the four diagonals). It is allowed to use the same die for different words, but it is not allowed to use the same die twice for the same word.

Each word earns points equal to the square of the length of the path. Points cannot be earned for the same word more than once, even if it appears multiple times on the board.

The project is implemented as an OOP class in Python, using the tkinter library.

## Table of context

- [Demo](#demo)
- [Copyright](#copyright)

## Demo



<img src="https://github.com/danielgibor/Boggle-Game/blob/main/README/boogle_game.gif" alt="Boggle Game GIF">
</p>

For a full demo video check this [link](https://www.youtube.com/watch?v=XJhGo_YWLI0).

<p align="right">(<a href="#about-the-project">back to top</a>)</p>

## Copyright

MIT License

Copyright (c) 2024 danielgibor

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

<p align="right">(<a href="#about-the-project">back to top</a>)</p>




