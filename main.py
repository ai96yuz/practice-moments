import asyncio

database = {
    1: {"name": "John Doe", "email": "john@example.com"},
    2: {"name": "Jane Smith", "email": "jane@example.com"},
}


async def search_users_in_db(query):
    await asyncio.sleep(1)
    results = []
    for user_id, user_info in database.items():
        if query.lower() in user_info["name"].lower():
            results.append(user_info)
    return results


async def handle_form_input():
    while True:
        user_input = input('Enter data : ')
        search_result = await search_users_in_db(user_input)
        if not search_result:
            print(f"No user with name '{user_input}' found. Please try again.")
        else:
            print(f"Search request complete: '{user_input}': {search_result}")

try:
    asyncio.run(handle_form_input())
except KeyboardInterrupt:
    print("\nExiting the program.")
