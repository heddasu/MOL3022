<script>
import { Bar} from 'vue-chartjs'


export default {
  extends: Bar,
  props: {
    chartdata: {
      type: Object,
      default: null,
    },
    options: {
            pan: {
              enabled: true,
              mode: "x"
            },
            zoom: {
              enabled: true,
              mode: "x"
            },
            legend: {
              display: false
            },
            maintainAspectRatio: false,
            scales: {
              xAxes: [
                {
                  barPercentage: 6,
                  scaleLabel: {
                    display: true,
                    labelString: "Posisjon"
                  },
                }
              ],
              yAxes: [
                {
                  scaleLabel: {
                    display: true,
                    labelString: "Score"
                  },
                  ticks: {
                    min: 0,
                    max: 300,
                    stepSize: 100,
                    reverse: false,
                    beginAtZero: true
                }
                }
              ]
            }}
          
  },
  mounted () {
    console.log(this.chartdata);
    if (this.chartdata) {
      this.renderChart({
        labels: this.chartdata.map((_, i) => (i + 1)),
        datasets: [{
          label: 'Probability',
          data: this.chartdata,
          backgroundColor: 'rgb(51, 204, 255)'
        }]
      }
      , this.options);
    }
  }
}
</script>

<style>
</style>