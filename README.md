# Django CRM & Analytics Platform

A production-oriented CRM platform built with Django, integrating authentication, contact synchronization, event tracking, time-series analytics, and automated workflows into a cohesive full-stack application.

## Overview

This project demonstrates the design and implementation of a modern Django application with an emphasis on modular architecture, relational data modeling, external API integration, analytics, and automation.

The system combines traditional CRM functionality with an event-driven tracking layer and time-series analytics infrastructure, providing a foundation for monitoring user activity and extracting temporal patterns from application data.

## Key Capabilities

* **Django application architecture** with relational models, foreign-key relationships, migrations, and modular services
* **Google OAuth authentication** and integration with the Google People API
* **Contact synchronization** with external data parsing and structured persistence
* **Event tracking system** using Django signals and generic relationships
* **Time-series analytics** powered by TimescaleDB and PostgreSQL
* **Temporal aggregation and analysis** for application events
* **Interactive data visualization** using Chart.js
* **Modern frontend layer** with Tailwind CSS, Flowbite, and Django templates
* **Custom Django management commands** for application-level automation
* **Automated workflows** using GitHub Actions
* **Modern Python tooling** with `uv` and pre-commit

## Architecture

The application is structured around several complementary layers:

**Application Layer**
Django handles business logic, routing, authentication, templates, and persistence.

**Integration Layer**
Google OAuth and the People API provide external authentication and contact synchronization capabilities.

**Analytics Layer**
Application events are stored and analyzed as time-series data using TimescaleDB, enabling efficient temporal aggregation and event analysis.

**Automation Layer**
Custom management commands and GitHub Actions automate recurring synchronization and operational tasks.

## Technologies

* Python
* Django
* PostgreSQL
* TimescaleDB
* Google OAuth 2.0
* Google People API
* Tailwind CSS
* Flowbite
* Chart.js
* GitHub Actions
* uv
* pre-commit

## Engineering Focus

The project focuses on integrating multiple production-oriented components within a single application while maintaining clear separation between application logic, external services, analytics infrastructure, and automation.

It provides practical experience with API-driven architectures, event-based data collection, time-series processing, authentication flows, database relationships, data visualization, and CI/CD-oriented automation.
