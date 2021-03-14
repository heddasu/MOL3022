<script>
import { Bar } from 'vue-chartjs'

export default {
  extends: Bar,
  props: ['chartdata', 'options'],
  mounted () {
    console.log(this.chartdata);
    if (this.chartdata) {
      this.renderChart({
        labels: this.chartdata.map((_, i) => (i + 1)),
        datasets: [{
          label: 'Probability for binding',
          data: this.chartdata,
          backgroundColor: ['rgba(255, 99, 132, 0.2)',]
        }],
      }, {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    });
    }
  }
}
</script>

<style>
</style>