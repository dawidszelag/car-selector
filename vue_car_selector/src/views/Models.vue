<template>
  <div class="content">
    <div class="box">
      <div class="box-title">
        CAR SUGGESTIONS
      </div>

      <div v-if="isDataLoading" class="center-content">
        <div class="lds-hourglass"></div>
      </div>
      <div v-else-if="modelList.length">
        <h2>We found {{ numberOfModels }} models that you might like</h2>
        <small>Select sub-model option to view sub-models.</small>
        <div class="box-content">
          <ModelCar v-for="item in modelList" :model-info="item" :key="item.id" class="model-box"/>
        </div>
      </div>
      <div class="center-content" v-else>
        nothing was found
      </div>
      <div class="navigation">

        <button
            class="button-back"
            @click="backToHome"
        >
          Back to form
        </button>
        <div>
          <span>Page {{ page }} of {{ parseInt(allPages) + 1 }}</span>
          <button
              class="button-next"
              v-on:click="page -= 1"
              :disabled="!(page>1)"
          >
            Previous
          </button>
          <button
              class="button-next"
              v-on:click="page +=1 "
              :disabled="!(page<(parseInt(allPages) + 1))"
          >
            Next
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import proper_query from "@/services/proper_query";
import axios from "axios";
import ModelCar from "@/components/ModelCar";
import router from "@/router";
import store from "@/store";

export default {
  name: "ModelResults",
  components: {ModelCar},
  data: function () {
    return {
      page: store.state.page_number_models,
      allPages: 0,
      modelList: [],
      numberOfModels: 0,
      isDataLoading: false,
    };
  },
  methods: {
    backToHome() {
      router.push({name: 'home'})
    },
    makeRequest() {
      this.isDataLoading = true;
      let params = proper_query();
      params.append('page', this.page.toString())
      axios.get('models', {params}).then(({data}) => {
        this.modelList = data.results
        this.numberOfModels = data.count
        this.allPages = this.numberOfModels / 24;
        this.isDataLoading = false
      }).catch(error => {
        this.isDataLoading = false
        console.log(error)
      })
    }
  },
  mounted() {
    this.makeRequest();
  },
  watch: {
    page() {
      store.state.page_number_models = this.page;
      this.makeRequest();
    }
  }
};
</script>
<style scoped>
h2 {
  margin-bottom: 0;
}

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
