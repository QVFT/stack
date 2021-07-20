// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ["Bin 1", "Bin 2", "Bin 3", "Bin 4"],
    datasets: [{
      data: [3.750, 2.750, 2, 1],
      backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc', '#ffa500'],
      hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf', '#ff8c00'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
      callbacks: {
        label: function(tooltipItem, chart) {
          return chart.labels[tooltipItem.index] + ": " + chart.datasets[0].data[tooltipItem.index] +  " lbs";
        }
      }
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});
