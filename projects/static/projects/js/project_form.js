// projects/static/projects/js/project_form.js

document.addEventListener('DOMContentLoaded', function() {
    // Global variables
    const stagesContainer = document.getElementById('stages-container');
    const stagesDataInput = document.getElementById('stages-data-input');
    const addStageBtn = document.getElementById('add-stage-btn');
    const stageTemplate = document.getElementById('stage-template');
    const taskTemplate = document.getElementById('task-template');
    const projectForm = document.getElementById('project-form');
    
    // Counter for stages
    let stageCounter = 0;
    
    // Load existing stages if any
    const stagesJsonElement = document.querySelector('script[type="application/json"]#stages-json');
    if (stagesJsonElement) {
        const stagesData = JSON.parse(stagesJsonElement.textContent);
        stagesData.forEach(stageData => {
            addStage(stageData);
        });
    }
    
    // Add stage button click handler
    addStageBtn.addEventListener('click', function() {
        addStage();
    });
    
    // Form submit handler
    projectForm.addEventListener('submit', function(e) {
        // Prevent form submission if there are no stages
        if (stagesContainer.children.length === 0) {
            e.preventDefault();
            alert('يجب إضافة مرحلة واحدة على الأقل');
            return;
        }
        
        // Collect all stages data
        const stagesData = collectStagesData();
        stagesDataInput.value = JSON.stringify(stagesData);
    });
    
    // Add a new stage to the container
    function addStage(stageData = null) {
        stageCounter++;
        
        // Clone the stage template
        const stageElement = document.importNode(stageTemplate.content, true).firstElementChild;
        
        // Set the stage number
        const stageNumber = stageData ? stageData.number : stageCounter;
        stageElement.querySelector('.stage-number').textContent = stageNumber;
        stageElement.querySelector('.stage-number-input').value = stageNumber;
        
        // Fill in stage data if provided
        if (stageData) {
            stageElement.querySelector('.stage-name').textContent = stageData.name;
            stageElement.querySelector('.stage-name-input').value = stageData.name;
            stageElement.querySelector('.stage-supervisor-input').value = stageData.supervisor;
            stageElement.querySelector('.stage-recipient-input').value = stageData.recipient;
            stageElement.querySelector('.stage-start-date-input').value = stageData.start_date;
            stageElement.querySelector('.stage-end-date-input').value = stageData.end_date;
        }
        
        // Set up event listeners for the stage
        setupStageEventListeners(stageElement);
        
        // Add the stage to the container
        stagesContainer.appendChild(stageElement);
        
        // Add tasks if provided
        if (stageData && stageData.tasks) {
            const tasksContainer = stageElement.querySelector('.tasks-container');
            stageData.tasks.forEach(taskData => {
                addTask(tasksContainer, taskData);
            });
        }
        
        // Update stage name when input changes
        const stageNameInput = stageElement.querySelector('.stage-name-input');
        stageNameInput.addEventListener('input', function() {
            stageElement.querySelector('.stage-name').textContent = this.value;
        });
        
        // Update stage numbers when stage number input changes
        const stageNumberInput = stageElement.querySelector('.stage-number-input');
        stageNumberInput.addEventListener('input', function() {
            stageElement.querySelector('.stage-number').textContent = this.value;
        });
        
        // Return the stage element
        return stageElement;
    }
    
    // Set up event listeners for a stage
    function setupStageEventListeners(stageElement) {
        // Remove stage button
        const removeStageBtn = stageElement.querySelector('.remove-stage-btn');
        removeStageBtn.addEventListener('click', function() {
            if (confirm('هل أنت متأكد من حذف هذه المرحلة؟')) {
                stageElement.remove();
                updateStageNumbers();
            }
        });
        
        // Add task button
        const addTaskBtn = stageElement.querySelector('.add-task-btn');
        const tasksContainer = stageElement.querySelector('.tasks-container');
        
        addTaskBtn.addEventListener('click', function() {
            addTask(tasksContainer);
        });
    }
    
    // Add a new task to a stage
    function addTask(tasksContainer, taskData = null) {
        // Clone the task template
        const taskElement = document.importNode(taskTemplate.content, true).firstElementChild;
        
        // Fill in task data if provided
        if (taskData) {
            taskElement.querySelector('.task-name').textContent = taskData.name;
            taskElement.querySelector('.task-name-input').value = taskData.name;
            taskElement.querySelector('.task-description-input').value = taskData.description || '';
        }
        
        // Set up remove task button
        const removeTaskBtn = taskElement.querySelector('.remove-task-btn');
        removeTaskBtn.addEventListener('click', function() {
            if (confirm('هل أنت متأكد من حذف هذه المهمة؟')) {
                taskElement.remove();
            }
        });
        
        // Update task name when input changes
        const taskNameInput = taskElement.querySelector('.task-name-input');
        taskNameInput.addEventListener('input', function() {
            taskElement.querySelector('.task-name').textContent = this.value;
        });
        
        // Add the task to the container
        tasksContainer.appendChild(taskElement);
        
        // Return the task element
        return taskElement;
    }
    
    // Update stage numbers after removal
    function updateStageNumbers() {
        const stages = stagesContainer.querySelectorAll('.stage-card');
        stages.forEach((stage, index) => {
            const number = index + 1;
            stage.querySelector('.stage-number').textContent = number;
            stage.querySelector('.stage-number-input').value = number;
        });
        
        // Update stage counter
        stageCounter = stages.length;
    }
    
    // Collect data from all stages
    function collectStagesData() {
        const stagesData = [];
        const stages = stagesContainer.querySelectorAll('.stage-card');
        
        stages.forEach((stage) => {
            const stageData = {
                number: stage.querySelector('.stage-number-input').value,
                name: stage.querySelector('.stage-name-input').value,
                supervisor: stage.querySelector('.stage-supervisor-input').value,
                recipient: stage.querySelector('.stage-recipient-input').value,
                start_date: stage.querySelector('.stage-start-date-input').value,
                end_date: stage.querySelector('.stage-end-date-input').value,
                tasks: []
            };
            
            // Collect tasks
            const tasks = stage.querySelectorAll('.task-item');
            tasks.forEach((task) => {
                const taskData = {
                    name: task.querySelector('.task-name-input').value,
                    description: task.querySelector('.task-description-input').value
                };
                
                stageData.tasks.push(taskData);
            });
            
            stagesData.push(stageData);
        });
        
        return stagesData;
    }
    
    // Add initial stage if none exist
    if (stagesContainer.children.length === 0) {
        addStage();
    }
});


