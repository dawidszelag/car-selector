<template>
  <div class="question">
    <h2 style="margin-bottom: 0">Which features are important to you?</h2>
    <h5 style="margin: 0 0 20px 0">Select at least 2, max X TBC so that we can better match the right car for you</h5>
    <div class="answers-box">
      <label class="option">
        <input
            type="checkbox"
            v-model="goofFuelEfficiency"
        />
        <font-awesome-icon
            icon="check-square"
        />
        <span>good fuel efficiency - below 10L/100 km</span>
      </label>

      <label class="option">
        <input
            type="checkbox"
            v-model="veryGoofFuelEfficiency"
        />
        <font-awesome-icon
            icon="check-square"
        />
        <span>very good fuel efficiency - below 7L/100 km</span>
      </label>
      <label class="option">
        <input
            type="checkbox"
            v-model="rangeOver400KM"
            value="400"
        />
        <font-awesome-icon
            icon="check-square"
        />
        <span>electric range - minimum 400 km</span>
      </label>
      <br>

      <label class="option">
        <input
            type="checkbox"
            v-model="firstTimeDriver"
        />
        <font-awesome-icon
            icon="check-square"
        />
        <span>first time driver</span>
      </label>

      <label class="option">
        <input
            type="checkbox"
            v-model="tallDriver"
        />
        <font-awesome-icon
            icon="check-square"
        />
        <span>tall driver(s) - over 1.9 m</span>
      </label>

    </div>
  </div>
</template>

<script>
export default {
  name: "Question16",
  data() {
    return {
      default_value: 6,
      default_value_2: 60,
    }
  },
  computed: {
    rangeOver400KM: {
      get() {
        return this.$store.state.query.electric_range;
      },
      set(value) {
        this.$store.state.query.electric_range = value;
      }
    },

    goofFuelEfficiency: {
      get() {
        return this.$store.state.query.goof_fuel_efficiency;
      },
      set(value) {
        if (value) {
          this.$store.state.query.very_goof_fuel_efficiency = false;
        }
        this.$store.state.query.goof_fuel_efficiency = value;
      }
    },

    veryGoofFuelEfficiency: {
      get() {
        return this.$store.state.query.very_goof_fuel_efficiency;
      },
      set(value) {
        if (value) {
          this.$store.state.query.goof_fuel_efficiency = false;
        }
        this.$store.state.query.very_goof_fuel_efficiency = value;
      }
    },


    tallDriver: {
      get() {
        return this.$store.state.query.tall_driver;
      },
      set(value) {
        this.$store.state.query.tall_driver = value;
      }
    },
    firstTimeDriver: {
      get() {
        return this.$store.state.query.first_time_driver;
      },
      set(value) {
        this.$store.state.query.first_time_driver = value;
      }
    },

  },


}
</script>

<style scoped>

</style>