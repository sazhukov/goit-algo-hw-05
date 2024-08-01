def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    result = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            return iterations, arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # шуканий елемент є наступним елементом після останнього 'left' індексу, якщо 'left' індекс не вийшов за межі масиву
    if left < len(arr):
        result = arr[left]

    return iterations, result

# Приклад використання:
sorted_array = [0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5, 1.7]
target_value = 1.8
result = binary_search(sorted_array, target_value)
print(result)  # Виведе (кількість ітерацій, верхня межа)
