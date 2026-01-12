from project import calculator, analyze_text, get_int

def test_calculator_add():
    assert calculator(2, 3, "add") == 5

def test_calculator_div():
    assert calculator(10, 2, "div") == 5

def test_analyze_text():
    result = analyze_text("hello world hello")
    assert result["words"] == 3
    assert result["unique_words"] == 2
