<template>
  <div>

    <div class="loading_screen-2">
      <div v-if="load_img" class="loading_box--white"></div>
      <div v-if="load_img" class="loading_box">
      </div>
    </div>

    <div class="loading_screen">
      <img class="img" v-on:load="onLoaded" src="@/assets/loading.png" alt="">
      <img class="img" src="@/assets/logo_name.png" alt="">
    </div>
  </div>
</template>

<script>
export default {
  name: "LoadingScreen",
  data() {
    return {
      load_img: false,
    }
  },
  methods: {
    onLoaded() {
      this.load_img = true
    },
  },
}
</script>

<style scoped>

.loading_screen-2,
.loading_screen {
  width: 100vw;
  height: 100vh;
  position: fixed;
  display: flex;
  justify-content: center;
  align-items: center;
  top: 0;
  left: 0;
  z-index: 9999;
}

.loading_screen-2 {
  background: #000;
}

.loading_screen {
  flex-direction: column;
}

.img {
  height: auto;
  width: 75%;
  z-index: 1;
}

.img:last-child {
  height: auto;
  opacity: 0;
  position: absolute;
  top: 55%;
  width: 25%;
  z-index: 100;
  animation: show_up;
  animation-delay: 2s;
  animation-duration: 3s;
  animation-fill-mode: forwards;
}

.loading_box--white {
  position: absolute;
  left: 0;
  content: '';
  width: 50vw;
  left: 25vw;
  height: 25vh;
  background: #000;
  animation-name: loading-bg;
  animation-duration: 7s;
  animation-fill-mode: forwards;
}

.loading_box {
  position: absolute;
  left: 0;
  content: '';
  width: 0;
  left: 25vw;
  height: 25vh;
  background: #000;
  animation-name: loading;
  animation-duration: 7s;
  animation-fill-mode: forwards;
}

@keyframes loading-bg {
  from {
    background: #fff;
  }
  to {
    background: #fff;
  }
}

@keyframes loading {
  from {
    width: 10vw;
    background: #ff005a;
  }
  to {
    width: 50vw;
    background: #ff005a;
  }
}

@keyframes show_up {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes show_down {s
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}

@media only screen and (max-width: 600px) {
  .loading_box--white {
    height: 150px;
  }

  .loading_box {
    height: 150px;
  }
}
</style>
