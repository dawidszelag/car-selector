<template>
  <div class="question">
    <h2>Do you have a brand in mind? Select all that apply</h2>
    <div class="answers-box">
      <label class="option" v-for="brand in brands" :key="brand.name">
        <div class="checkbox-option">
          <input
              type="checkbox"
              :checked="brandsList.includes(brand.id)"
              @change="addBrandToList(brand.id)"
          />
          <font-awesome-icon
              icon="check-square"
          />
          <span>{{ brand.name }}</span>
        </div>
        <div class="option-img">
          <img :src="brand.image" alt="">
        </div>
      </label>
    </div>

  </div>
</template>

<script>

export default {
  name: "Question5",
  data() {
    return {
      brands: [],
    }
  },
  methods: {
    clearList(value) {
      if (value) {
        this.$store.state.query.brands_list = []
      }
    },
    addBrandToList(brandId) {
      this.$store.state.query.brands_list.push(brandId)
    }
  },
  computed: {
    brandsList: function () {
      return this.$store.state.query.brands_list;
    }
  },
  created() {
    this.axios.get('brand').then(({data}) => {
      this.brands = data;
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

  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-start ;
}

.option-img{
  width: 50%;
}
.option-img img{
  max-width: 100%;
  height: auto;
  max-height: 45px;
}
.checkbox-option span{
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