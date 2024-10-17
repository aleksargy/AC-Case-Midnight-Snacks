# Case Study: The Relationship Between Midnight Snack Choices and Productivity

## Context:
Students across the university often indulge in midnight snacks while studying or procrastinating. The snack choices range from healthy options like fruits and nuts to indulgent treats like pizza, chips, and sugary sodas. The university administration is curious to find out whether these late-night snack choices have any impact on students' productivity, energy levels, and, most importantly, their meme-sharing abilities during group projects.

In this case study, your task is to analyse how midnight snack choices correlate with productivity, energy levels, and meme quality in group chats.

## Objective:
The objective of this study is to:
1. **Determine correlations** between midnight snack choices and next-day productivity levels.
2. **Analyze** whether healthier snacks lead to more energy or whether indulgent snacks inspire more creativity (memes).
3. **Provide recommendations** to students on how they can optimise their snack choices for maximum productivity and meme quality.

## Datasets:

1. **`students.csv`**: This dataset contains demographic and academic information for each student.
    - `student_id`: Unique identifier for each student.
    - `age`: The age of the student.
    - `major`: The academic major of the student.
    - `favorite_snack`: The student’s favorite midnight snack (e.g., pizza, chips, fruit, chocolate).
    - `meme_quality`: A self-reported score of the student's meme-sharing ability (1-10).

2. **`snack_consumption.csv`**: This dataset tracks each student's midnight snack choices over the last 7 days.
    - `student_id`: Unique identifier for each student.
    - `date`: The date of snack consumption.
    - `snack_type`: The type of snack consumed (e.g., "Pizza", "Fruit", "Chips", "Chocolate").
    - `quantity`: The number of snacks consumed (e.g., slices of pizza, pieces of fruit).

3. **`productivity.csv`**: This dataset tracks each student’s productivity the day after indulging in midnight snacks.
    - `student_id`: Unique identifier for each student.
    - `date`: The date of productivity measurement.
    - `hours_studied`: The number of hours the student studied the day after consuming midnight snacks.
    - `energy_level`: A self-reported energy level (1-10) the day after consuming snacks.
    - `memes_shared`: The number of memes shared in group chats the next day (serious metric, obviously).

## Guiding Questions:
1. **How do different midnight snack choices correlate with next-day productivity?**
   - Do students who eat healthier snacks study more or feel more energetic the next day? Or do pizza lovers secretly have more energy and focus?

2. **Is there a link between snack quantity and meme-sharing creativity?**
   - Does eating more pizza lead to a higher meme-sharing count the next day? Is chocolate the secret fuel for high-quality memes?

3. **Which snack types have the highest impact on energy levels?**
   - Do fruits and nuts boost energy levels? Or does indulging in chips give students the boost they need to survive long study hours?

4. **What snack recommendations should be given to students for balancing productivity and meme quality?**
   - Based on your findings, what snack choices should students make to balance their academic life and social contribution (via memes) to group projects?

## Optional Frontend:
Build a **"Midnight Snack Dashboard"** that allows students to:
- Track how different snack choices affect their next-day energy levels, productivity, and meme output.
- Input their snack choices and get snack recommendations based on past performance.
- Visualise the trends in snack choices across the student body and how these trends affect meme-sharing abilities during stressful group projects.

## Expected Outcome:
At the end of this project, students should:
- Identify the relationship between midnight snack choices and next-day productivity.
- Analyse how different snacks affect energy levels and meme quality.
- Provide actionable recommendations on which snacks boost productivity while allowing students to maintain their meme game.
- Make snack choices that balance studying with the vital art of meme creation.


