<h3 tabindex="-1" dir="auto">Проект по автоматизации тестирования ToolsQA, demoqa.com</h3>
<hr>
<h4 dir="auto"><em>Для запуска тестов необходимо:</em></h4>
<ol>
  <li>Скачать проект с удаленного репозитория на свой локальный, с помощью команды:<br>
    <code>git clone https://github.com/Aleks-QA/selenium_python_101internet.git</code></li>
  
  <li>Открыть проект на установленной заранее IDE,</li>
  
  <li>Создать и активировать виртуальное окружение:</li>
    <code>python -m venv venv</code></li><br>
    <code>venv\Scripts\activate</code></li>
    
  <li>Установить все зависимости: <br>
  <code>python -m pip install -r requirements.txt</code> 
  
  <li>Запустить тесты командой:<br><code>python -s -m pytest --alluredir=test_results</code> </li>
  
  <li>Открыть отчет о прохождении тестов командой:<br>
    <code>allure serve test_results/ </code></li>
</ol>

