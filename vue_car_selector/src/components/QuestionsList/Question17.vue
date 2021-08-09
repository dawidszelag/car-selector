<template>
  <div class="question">
    <h2 style="margin-bottom: 0">Which features are important to you?</h2>
    <h5 style="margin: 0 0 20px 0">Select at least 2, max X TBC so that we can better match the right car for you</h5>
    <div class="answers-box">
      <label class="option">
        <input
            type="checkbox"
            v-model="sportFeel"
        />
        <font-awesome-icon
            icon="check-square"
        />
        <span>sporty feel</span>
      </label>
      <label class="option">
        <input
            type="checkbox"
            v-model="handling"
        />
        <font-awesome-icon
            icon="check-square"
        />
        <span>handling dynamics</span>
      </label>
      <label class="option">
        <input
            type="checkbox"
            v-model="raceTrack"
        />
        <font-awesome-icon
            icon="check-square"
        />
        <span>race track capacity</span>
      </label>
      <br>

      <label class="option">
        <input
            type="checkbox"
            v-model="powerOver200"
        />
        <font-awesome-icon
            icon="check-square"
        />
        <span>power minimum 200 hp/149 KW</span>
      </label>
      <label class="option">
        <input
            type="checkbox"
            v-model="powerOver300"
        />
        <font-awesome-icon
            icon="check-square"
        />
        <span>power minimum 300 hp/224 kW</span>
      </label>
      <label class="option">
        <input
            type="checkbox"
            v-model="accelerationUnder5"
        />
        <font-awesome-icon
            icon="check-square"
        />
        <span>acceleration under 5 seconds</span>
      </label>
      <label class="option">
        <input
            type="checkbox"
            v-model="accelerationUnder8"
        />
        <font-awesome-icon
            icon="check-square"
        />
        <span>acceleration under 8 seconds</span>
      </label>

    </div>
  </div>
</template>

<script>
export default {
  name: "Question17",
  data() {
    return {
      default_value: 6,
      default_value_2: 60,
    }
  },
  computed: {

    sportFeel: {
      get() {
        return this.$store.state.query.sport_feel;
      },
      set(value) {
        this.$store.state.query.sport_feel = value;
      }
    },

    handling: {
      get() {
        return this.$store.state.query.handling;
      },
      set(value) {
        this.$store.state.query.handling = value;
      }
    },

    raceTrack: {
      get() {
        return this.$store.state.query.race_track;
      },
      set(value) {
        this.$store.state.query.race_track = value;
      }
    },

    powerOver300: {
      get() {
        return this.$store.state.query.power_over_300;
      },
      set(value) {
        if (value) {
          this.$store.state.query.power_over_200 = false;
        }
        this.$store.state.query.power_over_300 = value;
      }
    },

    powerOver200: {
      get() {
        return this.$store.state.query.power_over_200;
      },
      set(value) {
        if (value) {
          this.$store.state.query.power_over_300 = false;
        }
        this.$store.state.query.power_over_200 = value;
      }
    },

    accelerationUnder5: {
      get() {
        return this.$store.state.query.acceleration_under_5;
      },
      set(value) {
        if (value) {
          this.$store.state.query.acceleration_under_8 = false;
        }
        this.$store.state.query.acceleration_under_5 = value;
      }
    },
    accelerationUnder8: {
      get() {
        return this.$store.state.query.acceleration_under_8;
      },
      set(value) {
        if (value) {
          this.$store.state.query.acceleration_under_5 = false;
        }
        this.$store.state.query.acceleration_under_8 = value;
      }
    },
  },


}
</script>

<style scoped>

</style>