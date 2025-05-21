// Wait for DOM to load completely
document.addEventListener('DOMContentLoaded', function() {
    // Get form element
    const predictionForm = document.getElementById('predictionForm');
    
    // Handle form submission
    predictionForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Show loading spinner
        document.getElementById('initialMessage').classList.add('d-none');
        document.getElementById('resultContainer').classList.add('d-none');
        document.getElementById('loadingSpinner').classList.remove('d-none');
        
        // Get form data
        const formData = new FormData(predictionForm);
        
        // Send prediction request
        fetch('/predict', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Hide loading spinner
            document.getElementById('loadingSpinner').classList.add('d-none');
            
            // Show result container
            const resultContainer = document.getElementById('resultContainer');
            resultContainer.classList.remove('d-none');
            
            // Update prediction result
            const predictionResult = document.getElementById('predictionResult');
            const probabilityResult = document.getElementById('probabilityResult');
            
            if (data.prediction === 1) {
                predictionResult.textContent = 'Survived';
                predictionResult.className = 'mt-3 display-6 survived';
            } else {
                predictionResult.textContent = 'Did Not Survive';
                predictionResult.className = 'mt-3 display-6 not-survived';
            }
            
            // Format probability as percentage
            const probability = (data.probability * 100).toFixed(2);
            probabilityResult.textContent = `Survival Probability: ${probability}%`;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('loadingSpinner').classList.add('d-none');
            document.getElementById('initialMessage').classList.remove('d-none');
            document.getElementById('initialMessage').innerHTML = `<p class="text-danger">Error: ${error.message}</p>`;
        });
    });
    
    // Load statistics when page loads
    loadStatistics();
});

// Function to load statistics
function loadStatistics() {
    // Show loading spinner for stats
    document.getElementById('statsContent').classList.add('d-none');
    document.getElementById('statsLoading').classList.remove('d-none');
    
    // Fetch statistics data
    fetch('/stats')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Hide loading spinner
            document.getElementById('statsLoading').classList.add('d-none');
            
            // Show stats content
            document.getElementById('statsContent').classList.remove('d-none');
            
            // Update statistics
            document.getElementById('overallSurvival').textContent = `${data.survival_rate.toFixed(2)}%`;
            
            // Update gender statistics
            const maleBar = document.getElementById('maleSurvival');
            const femaleBar = document.getElementById('femaleSurvival');
            maleBar.style.width = `${data.male_survival}%`;
            femaleBar.style.width = `${data.female_survival}%`;
            document.getElementById('malePercent').textContent = `${data.male_survival.toFixed(2)}%`;
            document.getElementById('femalePercent').textContent = `${data.female_survival.toFixed(2)}%`;
            
            // Update age group statistics
            const childrenBar = document.getElementById('childrenSurvival');
            const adultBar = document.getElementById('adultSurvival');
            const elderlyBar = document.getElementById('elderlySurvival');
            childrenBar.style.width = `${data.children_survival}%`;
            adultBar.style.width = `${data.adult_survival}%`;
            elderlyBar.style.width = `${data.elderly_survival}%`;
            document.getElementById('childrenPercent').textContent = `${data.children_survival.toFixed(2)}%`;
            document.getElementById('adultPercent').textContent = `${data.adult_survival.toFixed(2)}%`;
            document.getElementById('elderlyPercent').textContent = `${data.elderly_survival.toFixed(2)}%`;
            
            // Update class statistics
            const class1Bar = document.getElementById('class1Survival');
            const class2Bar = document.getElementById('class2Survival');
            const class3Bar = document.getElementById('class3Survival');
            class1Bar.style.width = `${data.class1_survival}%`;
            class2Bar.style.width = `${data.class2_survival}%`;
            class3Bar.style.width = `${data.class3_survival}%`;
            document.getElementById('class1Percent').textContent = `${data.class1_survival.toFixed(2)}%`;
            document.getElementById('class2Percent').textContent = `${data.class2_survival.toFixed(2)}%`;
            document.getElementById('class3Percent').textContent = `${data.class3_survival.toFixed(2)}%`;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('statsLoading').classList.add('d-none');
            document.getElementById('statsContainer').innerHTML = `<p class="text-danger">Error loading statistics: ${error.message}</p>`;
        });
} 