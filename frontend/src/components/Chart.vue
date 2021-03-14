<template>
  <div class="container">
    <line-chart
      v-if="loaded"
      :chartdata="chartdata"
      :options="options"/>
  </div>
</template>

<script>
import BarChart from './Chart.vue'
import { Bar } from 'vue-chartjs'
//import results from 'input.vue'

export default {
  name: 'BarChartContainer',
  components: { BarChart },
  extends: Bar,
  props: {
    chartdata: {
      type: Object,
      default: null
    },
    options: {
      type: Object,
      default: null
    },
  data: () => ({
    loaded: false,
    chartdata: null,
    labels: ["2015-01", "2015-02", "2015-03", "2015-04", "2015-05", "2015-06", "2015-07", "2015-08", "2015-09", "2015-10", "2015-11", "2015-12"],
    datasets: [{
      label: "# of Tomatoes",
      data: [12, 19, 3, 5, 2, 3, 20, 3, 5, 6, 2, 1]}]
  }),
  async mounted () {
    this.loaded = false
    try {
      //const { userlist } = await fetch('/api/userlist')
      //this.chartdata = userlist
      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  },
  mounted () {
    this.renderChart(this.chartdata, this.options)
  }
  }
}
</script>