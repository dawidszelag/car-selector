<template>
  <div class="content">
    <div class="box">
      <div class="box-title">
        Select submodel
      </div>
      <h2>{{ modelName }}</h2>
      <div v-if="isDataLoading" class="center-content">
        <div class="lds-hourglass"></div>
      </div>
      <div   v-else-if="subModelList.length" class="box-content">
        <SubModelCar v-for="item in subModelList" :car-info="item" :key="item.id" class="model-box"/>
      </div>
      <div class="navigation">

        <button
            class="button-back"
            @click="backToModels"
        >
          Back
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import proper_query from "@/services/proper_query";
import axios from "axios";
import SubModelCar from "@/components/SubModelCar";

export default {
  name: "ModelResults",
  components: {SubModelCar},
  data: function () {
    return {
      modelId: this.$route.params.modelId,
      subModelList: [],
      modelName: '',
      isDataLoading: false,
    };
  },
  methods: {
    backToModels() {
      this.$router.push({name: 'models'})
    },
    makeRequest() {
      this.isDataLoading =  true;
      let params = proper_query();
      params.append('model', this.modelId.toString())
      axios.get('cars-list', {params}).then(({data}) => {
        this.subModelList = data.results
        console.log(data)
        this.modelName = data.results[0].model.brand.name + ' ' + data.results[0].model.name;
        this.isDataLoading =  false;
      }).catch(error => {
        this.isDataLoading =  true;
        console.log(error)
      })
    }
  },
  mounted() {
    this.makeRequest();
  },
  watch: {
    page() {
      this.makeRequest();
    }
  }
};
</script>
<style scoped>
small {
  display: inline-block;
  font-size: 14px;
  margin-bottom: 20px;
}

.content {
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding-top: 200px;
  padding-bottom: 100px;
  min-height: 100vh;
  flex: 1;
}

.box {
  width: 80%;
  max-width: 650px;
}

.box-content {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}

.box-title {
  color: #ff005a;
  font-weight: 600;
  margin-bottom: 10px;
}

.model-box {
  width: 47%;
  margin-bottom: 25px;
}

.navigation {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 20px;
}

.navigation button {
  padding: 8px 15px;
  font-size: 12px;
}

.navigation span {
  font-size: 13px;
  font-weight: 700;
}
</style> 
