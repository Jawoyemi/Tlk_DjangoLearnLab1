# 📝 Tlk_DjangoLearnLab

## Week 3: Forms & CRUD  
**Project:** Personal Blog - Part 2 (Full CRUD)

This project implements a simple personal blog application with **Create**, **Read**, **Update**, and **Delete (CRUD)** functionality using **Django ModelForms**.  
It also includes admin customization and basic frontend templates for managing blog posts.

---

## 📂 Project Structure
Tlk_DjangoLearnLab/
├── django_blog/
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── templates/
│ │ ├── base.html
│ │ ├── post_list.html
│ │ ├── post_detail.html
│ │ ├── post_form.html
│ │ ├── post_confirm_delete.html
│ ├── urls.py
│ ├── views.py
│ └── migrations/
└── README.md

---

## 🎯 Features & Requirements

### ✅ Admin Customization
- The `Post` model is registered in `admin.py`.
- A superuser can create, update, and delete posts via the Django admin interface.

### ✅ Read Functionality
- Implemented using a **PostListView**.
- Posts are displayed from **newest to oldest**.

### ✅ Create Functionality
- Implemented with **PostCreateView** using **ModelForm**.
- Includes `{% csrf_token %}` for security.
- Successfully handles POST requests.
- Redirects to the **post list page** after creation.

### ✅ Detail & Update Functionality
- **PostDetailView** displays a single post using `get_object_or_404`.
- **PostUpdateView** prepopulates the form with existing data and updates the post on submission.

### ✅ Delete Functionality
- **PostDeleteView** confirms deletion and removes the post from the database.
- Delete and update buttons are included on the `post_detail.html` page.

---

