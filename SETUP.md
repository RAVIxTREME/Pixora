# InstaClone — Full Setup Guide

## Folder Structure (apne project mein ye banao)

```
your_project/
├── posts/
│   ├── models.py         ← already done (Phase 1)
│   ├── views.py          ← posts_views.py ka content paste karo
│   ├── urls.py           ← posts_urls.py ka content paste karo
│   └── templates/
│       └── posts/
│           ├── home.html
│           ├── explore.html
│           ├── create_post.html
│           ├── post_detail.html
│           └── profile.html
└── templates/
    └── base.html         ← base.html paste karo yahan
```

## Step 1 — views.py
posts_views.py ka pura content `posts/views.py` mein paste karo

## Step 2 — urls.py
posts_urls.py ka pura content `posts/urls.py` mein paste karo

## Step 3 — Templates
- base.html → `templates/base.html`
- baaki sab → `posts/templates/posts/` folder mein

## Step 4 — settings.py check karo
```python
TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'templates'],  # ye line honi chahiye
        ...
    }
]
```

## Step 5 — Run karo
```bash
python manage.py runserver
```

## Pages:
- `/`           → Home feed
- `/explore/`   → All posts grid
- `/post/create/` → New post
- `/profile/username/` → User profile

## Notes:
- Auth wali login/logout URLs already hain teri project mein ✅
- UserProfile model already hai ✅
- Sirf posts app ka views + urls + templates add karna hai
