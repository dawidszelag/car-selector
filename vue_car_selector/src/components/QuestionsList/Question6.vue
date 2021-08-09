<template>
  <div class="question">
    <h2>Which body types would you like? Select all that apply</h2>
    <div class="answers-box">
      <label class="option" v-for="body in bodies" :key="body.name">
        <div class="checkbox-option">
          <input
              type="checkbox"
              :checked="bodiesList.includes(body.id)"
              @change="addBodiesToList(body.id)"
          />
          <font-awesome-icon
              icon="check-square"
          />
          <span>{{ body.name }}</span>
        </div>
        <div class="option-img">
          <img :src="body.image" alt="">
        </div>
      </label>
    </div>
  </div>
</template>

<script>

export default {
  name: "Question6",
  data() {
    return {
      bodies: [],
    }
  },
  methods: {
    addBodiesToList(bodyId) {
      this.$store.state.query.bodies_list.push(bodyId)
    }
  },
  computed: {
    bodiesList: function () {
      return this.$store.state.query.bodies_list;
    }
  },
  created() {
    this.axios.get('body').then(({data}) => {
      this.bodies = data;
    })
  }
}
</script>

<style scoped>
.answers-box {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.option {
  width: 32%;
  display: flex;
  min-height: 80px;
  justify-content: space-between;

}

.checkbox-option {
  max-width: 45%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-start;

}

.option-img {
  width: 50%;
}

.option-img img {
  max-width: 100%;
  height: auto;
  max-height: 45px;
}

.checkbox-option span {
  min-width: 100%;
  margin-top: 10px;
  font-size: 12px;
  margin-left: 5px;
  word-break: break-all;
}

input {
  width: 70%;
  cursor: pointer;
}

@media only screen and (max-width: 992px) {
  .option {
    width: 49%;
  }

}

</style>