<template>
  <div class="question">
    <h2>What is your budget?</h2>
    <div class="answers-box">
    <label class="option">
      <input type="range" v-model="budget"
             :min="min_price" :max="max_price" step="10">
      <span class="budget-info">${{ budget }}</span>
    </label>
  </div>
  </div>
</template>

<script>
export default {
  name: "Question4",
  data() {
    return {
      max_price: 0,
      min_price: 0,
    }
  },
  computed: {
    budget: {
      get() {
        return this.$store.state.query.budget;
      },
      set(value) {
        this.$store.state.query.budget = value;
      }
    },
  },
  mounted() {
    this.axios.get('budget').then(({data}) => {
      this.max_price = data.max_price;
      this.min_price = data.min_price;
      if (this.$store.state.query.budget){
        this.budget = this.$store.state.query.budget;
      } else{
        this.budget = data.min_price;
      }
    })
  }
}
</script>

<style scoped>
input {
  width: 70%;
  cursor: pointer;
}

.budget-info {
  width: 30%;
  text-align: right;
}
</style>