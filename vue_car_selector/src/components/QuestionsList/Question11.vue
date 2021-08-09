<template>
  <div class="question">
    <h2>What's the minimum boot space you need?</h2>
    <div class="answers-box">
      <label class="option">
        <input
            type="radio"
            v-model="boot"
            value="1"

        />
        <font-awesome-icon
            icon="check-circle"
        />
        <span>Any</span>
      </label>

      <label class="option">
        <input
            type="radio"
            v-model="boot"
            value="120"
        />
        <font-awesome-icon
            icon="check-circle"
        />
        <span>1 suitcase - 120 litres</span>
      </label>

      <label class="option">
        <input
            type="radio"
            v-model="boot"
            value="240"
        />
        <font-awesome-icon
            icon="check-circle"
        />
        <span>2 suitcases - 240 litres</span>
      </label>
      <label class="option">
        <input
            type="radio"
            v-model="boot"
            value="360"
        />
        <font-awesome-icon
            icon="check-circle"
        />
        <span>3 suitcases - 360 litres</span>
      </label>
      <label class="option">
        <input
            type="radio"
            v-model="boot"
            value="480"
        />
        <font-awesome-icon
            icon="check-circle"
        />
        <span>4 suitcases - 480 litres</span>
      </label>
      <label class="option">
        <input
            type="radio"
            v-model="boot"
            value="600"
        />
        <font-awesome-icon
            icon="check-circle"
        />
        <span>5 suitcases - 600 litres</span>
      </label>
    </div>
  </div>
</template>

<script>
export default {
  name: "Question11",
  watch: {
    boot() {
      this.$store.state.question_11 = parseInt(this.boot)
    }
  },
  computed: {
    boot: {
      get() {
        return this.$store.state.question_11;
      }
      ,
      set(value) {
        this.$store.state.question_11 = value;
      }

    }
  }

}
</script>

<style scoped>

</style>