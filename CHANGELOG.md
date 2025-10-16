# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- refactored code, e.g. datum.py
- added __str__ and __repr__ method to different classes to make it
  easier to work on the command line with these objects

### Added
- more tests for parsing input files
- set_seed function
- set_nps function
- code examples
- parsing of more output data

## [0.2.0]  - 2024-10-27

### Fixed
- fixed from_mcnp and to_mcnp for several classes
- fixed pre-commit
- fixed CI

### Added
- more tests for parsing input files
- examples
- material.from_formula
- modify function to change inp objects

### Changed
- updated docs
- better __str__ and __repr__ for several classes
- updated cli

## [0.1.2]  - 2024-10-19

### Fixed
- CI: automated release on PyPI

## [0.1.1]  - 2024-10-19

Initial release. Not everything is working yet ;)

