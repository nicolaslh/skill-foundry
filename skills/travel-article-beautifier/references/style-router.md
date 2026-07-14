# Style Router

Use this router before selecting a style template. The goal is to choose the best AI-readable prompt template from `references/style-templates/` based on the user's source material, target reader, and requested output.

## Routing Steps

1. Read the user's request and source notes.
2. Identify dominant intent: reflection, city editorial, route clarity, photo sequence, or practical planning.
3. Match recognition signals to one primary style template.
4. Select one optional secondary influence only when it improves the output.
5. State the selected style briefly in the working brief.

## Primary Styles

### field-journal

Choose when the source is slow, reflective, personal, seasonal, nature-adjacent, or diary-like.

Strong signals:

- "日记", "手账", "慢旅行", "山里", "海边", "古镇", "雨天", "清晨", "黄昏"
- The user emphasizes mood, memory, weather, walking, solitude, quiet scenes, or small details.

Avoid when the user mostly needs checklists, route optimization, or dense recommendations.

### city-magazine

Choose when the source is urban, stylish, editorial, lifestyle-oriented, or recommendation-heavy.

Strong signals:

- City walk, neighborhood, cafe, restaurant, design hotel, bookstore, gallery, shop
- The user asks for "杂志感", "高级", "小众", "city walk", "生活方式", "标题吸引人"

Avoid when route order is essential or the article is mainly a personal diary.

### route-map

Choose when movement and sequence are the main value.

Strong signals:

- Day-by-day notes, multi-city travel, road trip, train route, hiking route, island hopping
- The user provides stops, dates, transfers, distances, or route order.

Avoid when the source is mostly image captions or one-place reflection.

### minimal-gallery

Choose when images or captions are the primary material.

Strong signals:

- User provides photos, image captions, shot lists, gallery request, visual diary request
- The article should be minimal, cinematic, quiet, or image-first.

Avoid when the reader needs dense planning advice.

### practical-guide

Choose when the article must help readers plan.

Strong signals:

- "攻略", "路线", "避坑", "亲子", "预算", "交通", "住宿", "餐厅", "清单"
- User asks for practical, scannable, structured, or checklist-like output.

Avoid when the user wants a purely literary travel essay.

## Secondary Influences

Use a secondary influence only as a modifier:

- `field-journal + practical-guide`: reflective article with a clean planning appendix.
- `city-magazine + minimal-gallery`: stylish urban piece with strong captions.
- `route-map + practical-guide`: itinerary-first guide.
- `minimal-gallery + field-journal`: quiet visual diary.

Do not combine more than two styles unless the user explicitly asks.

## Tie Breakers

- If route order matters, prefer `route-map`.
- If the output is for readers planning the same trip, prefer `practical-guide`.
- If the user supplied many photos or captions, prefer `minimal-gallery`.
- If the user asks for "美文", "散文", or "氛围感", prefer `field-journal`.
- If the user asks for "杂志感", "小红书高级感", or urban lifestyle, prefer `city-magazine`.

## Router Output

Add this to the working brief:

```markdown
## Style Decision

- Primary style: <style-id>
- Secondary influence: <optional style-id or none>
- Why: <one sentence>
- Template path: references/style-templates/<style-id>.md
```
