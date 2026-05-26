import pytest
def test_numbers():
    numbers = [1, 2, 3, 4, 5]
    assert len(numbers) == 5
def test_spisok():
    numbers = [1, 2, 3, 4, 5]
    assert numbers[0] == 1
    assert numbers[-1] == 5
def test_words():
    words = ["hello", "world"]
    words.append("python")
    assert len(words) == 3
def test_numbs():
    numbers = [3, 1, 4, 1, 5]
    sorted_numbers = sorted(numbers)
    assert sorted_numbers[0] == 1
def test_emails():
    emails = ["a@b.com", "c@d.com"]
    assert all("@" in email for email in emails)

