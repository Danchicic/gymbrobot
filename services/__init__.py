import asyncio

multipliers = {
    0: (0.7, "10"),
    1: (0.75, "8"),
    2: (0.88, "4-6"),
    3: (0.93, "2-4"),
    4: (0.65, "6"),
}


async def unparse_user_workout(workout: str):
    strings = workout.split('\n')
    workout_data = {}

    for i, exercise in enumerate(strings):
        exercise = exercise.strip()
        if len(exercise.split('-')) == 1:
            if workout_data:
                yield workout_data
            day = exercise
            workout_data['day'] = day
            workout_data['exercises'] = {}
            continue
        name, max_weight = exercise.split('-')
        workout_data['exercises'] = workout_data.get('exercises', {}) | {name.strip(): int(max_weight)}
    yield workout_data


async def main():
    async for ex in unparse_user_workout("""Monday
Vertical thrust - 80 
Horizontal thrust - 60
Pull up - 30
Tuesday
Push down -  25"""):
        print(ex)


if __name__ == '__main__':
    asyncio.run(main())
