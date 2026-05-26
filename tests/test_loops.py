import pytest
def test_number():
    numbers = [1, 2, 3, 4, 5]
    total = sum(numbers)
    assert total == 15
def test_spisok():
    numbers = [1, 2, 3, 4, 5]
    even = [n for n in numbers if n % 2 == 0]
    assert len(even) == 2
def test_words():
    words = ["api", "test", "automation"]
    assert all(len(w) > 2 for w in words)
def test_p():
    numbers = [1, 2, 3, 4, 5]
    assert max(numbers) == 5
def test_email():
    emails = ["a@b.com", "", "c@d.com"]
    non_empty = [e for e in emails if e]
    assert len(non_empty) == 2