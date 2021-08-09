<template>
  <div class="question">
    <h2>What car size would you like? Select all that apply</h2>
    <div class="answers-box">
    <label class="option">
      <input
          type="checkbox"
          v-model="compact"

      />
      <font-awesome-icon
          icon="check-square"
      />
      <span>compact</span>
    </label>

    <label class="option">
      <input
          type="checkbox"
          v-model="medium"
      />
      <font-awesome-icon
          icon="check-square"
      />
      <span>medium</span>
    </label>

    <label class="option">
      <input
          type="checkbox"
          v-model="large"
      />
      <font-awesome-icon
          icon="check-square"
      />
      <span>large</span>
    </label>
    <label class="option">
      <input
          type="checkbox"
          v-model="unsure"
      />
      <font-awesome-icon
          icon="check-square"
      />
      <span>unsure</span>
    </label>
  </div>
  </div>
</template>

<script>
export default {
  name: "Question7",
  data() {
    return {
      unsure: false,
    }
  },
  computed: {
    compact: {
      get() {
        return this.$store.state.query.compact;
      },
      set(value) {
        if (value) {
          this.unsure = false;
        }
        this.$store.state.query.compact = value;
      }

    },
    medium: {
      get() {
        return this.$store.state.query.medium;
      },
      set(value) {
        if (value) {
          this.unsure = false;
        }
        this.$store.state.query.medium = value;
      }
    },
    large: {
      get() {
        return this.$store.state.query.large;
      },
      set(value) {
        if (value) {
          this.unsure = false;
        }
        this.$store.state.query.large = value;
      }
    },
  },
  watch: {
    unsure() {
      if (this.unsure) {
        this.compact = false;
        this.medium = false;
        this.large = false;
      }
    }
  }

}
</script>

<style scoped>

</style>