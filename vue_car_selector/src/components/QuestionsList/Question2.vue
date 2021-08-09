<template>
  <div class="question">
    <h2>Age group of the driver(s) - select all that apply</h2>
    <div class="answers-box">
    <label class="option">
      <input
          type="checkbox"
          v-model="youngDriver"

      />
      <font-awesome-icon
          icon="check-square"
      />
      <span>16-23</span>
    </label>

    <label class="option">
      <input
          type="checkbox"
          v-model="driver23_45"
      />
      <font-awesome-icon
          icon="check-square"
      />
      <span>23-45</span>
    </label>
    <label class="option">
      <input
          type="checkbox"
          v-model="middleAgedDriver"
      />
      <font-awesome-icon
          icon="check-square"
      />
      <span>45-60</span>
    </label>

    <label class="option">
      <input
          type="checkbox"
          v-model="olderDriver"
      />
      <font-awesome-icon
          icon="check-square"
      />
      <span>60+</span>
    </label>
  </div>
  </div>
</template>

<script>
export default {
  name: "Question2",
  computed: {
    youngDriver: {
      get() {
        return this.$store.state.query.young_driver;
      },
      set(value) {
        this.$store.state.query.young_driver = value;
      }

    },
    driver23_45: {
      get() {
        return this.$store.state.query.driver_23_45;
      },
      set(value) {
        this.$store.state.query.driver_23_45 = value;
      }
    },
    middleAgedDriver: {
      get() {
        return this.$store.state.query.middle_aged_driver;
      },
      set(value) {
        this.$store.state.query.middle_aged_driver = value;
      }
    },
    olderDriver: {
      get() {
        return this.$store.state.query.older_driver;
      },
      set(value) {
        this.$store.state.query.older_driver = value;
      }
    },
  },

}
</script>

<style scoped>

</style>