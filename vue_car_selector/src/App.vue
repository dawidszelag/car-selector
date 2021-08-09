<template>
  <div class="container">
    <FullScreenVideoBG/>
    <LoadingScreen v-if="isLoading"></LoadingScreen>
    <div class="main-content">
      <InfoBox/>
      <router-view/>
    </div>
  </div>
</template>

<script>
import "@/assets/styles.css";
import FullScreenVideoBG from "@/components/FullScreenVideoBG.vue";
import InfoBox from "@/components/InfoBox.vue";
import LoadingScreen from "./components/LoadingScreen";


export default {
  name: "App",
  data() {
    return {
      isLoading: true
    };
  },
  components: {
    LoadingScreen,
    FullScreenVideoBG,
    InfoBox,
  },
  mounted() {
    setTimeout(() => {
      this.isLoading = false;
    }, 5000);
  }
};
</script>
<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Mr+De+Haviland&display=swap");

.main-content {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  margin-bottom: -100px;
}

.fade-enter {
  opacity: 0;
}

.fade-enter-active {
  transition: opacity 2s ease;
}

.fade-leave {
}

.fade-leave-active {
  transition: opacity 2s ease;
  opacity: 0;
}

@media only screen and (max-width: 992px) {
  .main-content {
    flex-direction: column;
  }
}


</style> 
