---
layout: post
title: Example of all image tools
no_menu_item: true # required only for this example website because of menu construction
support: [jquery, gallery]
---

## Single Image, clickable for full screen
{% include clickimg.html image_path="assets/photography/san-francisco/VS-2012-5930-6000x4000.jpg" thumb_path="assets/photography/san-francisco/VS-2012-5930-thumbnail.jpg" alt="plop" %}

## Diaporama, clickable for full screen
{% include lightslider.html gallery=site.data.galleries.san-francisco %}

## Gallery, clickable for full screen
{% include gallery-layout.html gallery=site.data.galleries.san-francisco %}
