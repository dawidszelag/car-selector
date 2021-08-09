<template>
  <div class="question">
    <h2>What drive line would you like?</h2>
    <div class="answers-box">
      <label class="option">
        <input
            type="radio"
            v-model="drive"
            value="All Wheel Drive"

        />
        <font-awesome-icon
            icon="check-circle"
        />
        <span>All Wheel Drive</span>
      </label>

      <label class="option">
        <input
            type="radio"
            v-model="drive"
            value="Front Wheel Drive"
        />
        <font-awesome-icon
            icon="check-circle"
        />
        <span>Front Wheel Drive</span>
      </label>

      <label class="option">
        <input
            type="radio"
            v-model="drive"
            value="Rear Wheel Drive"
        />
        <font-awesome-icon
            icon="check-circle"
        />
        <span>Rear Wheel Drive</span>
      </label>
    </div>
  </div>
</template>

<script>
export default {
  name: "Question12",
  watch: {
    drive() {
      this.$store.state.question_12 = this.drive;
    }

  },
  computed: {
    drive: {
      get() {
        return this.$store.state.question_12;
      }
      ,
      set(value) {
        this.$store.state.question_12 = value;
      }

    }
  }

}
</script>

<style scoped>

</style>