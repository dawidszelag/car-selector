<template>
  <div>
    <div class="models_results">
      <div class="model_view">
        <div class="model_img">
          <div v-if="modelInfo.image" class="img" v-bind:style="modelImg"> </div>
          <div v-else class="img" style="background: url('https://via.placeholder.com/800x500') no-repeat center;"> </div>
          <div class="model_name">{{ modelInfo.brand }} {{ modelInfo.name }}</div>
        </div>
        <button @click="viewSubModel" class="btn_view">VIEW: {{ modelInfo.number_of_cars }} SUB-MODELS</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ModelCar",
  props: ['modelInfo',],
  data() {
    return {
      baseUrl: this.$store.state.base_media_url,
    }
  },
  methods: {
    viewSubModel() {
      this.$router.push({name: 'sub-models', params: {modelId: this.modelInfo.id}})
    }
  },
  computed: {
    modelImg: function () {
      return {
        background: `url(${this.baseUrl}${this.modelInfo.image}) no-repeat center`,
      }
    }
  }
}
</script>

<style scoped>

.models_results {
  width: 100%;
  display: flex;
  flex-wrap: wrap;
}

.model_view .img {
  width: 100%;
  min-height: 180px;
  margin-bottom: 5px;
  background-size: cover;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
}

.model_view {

  min-width: 100%;
}

.model_view .model_img {
  position: relative;
}

.model_view .model_img .model_name {
  position: absolute;
  bottom: 10px;
  left: 10px;
  font-weight: 700;
}

.model_view .btn_view {
  width: 100%;
  height: 40px;
  background: #ff005a;
  border: none;
  color: white;
  opacity: 0.8;
  font-weight: 600;

}

.model_view .btn_view:hover {
  opacity: 1;
  cursor: pointer;
}
</style>