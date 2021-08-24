<template>
  <div>
    <div class="fullscreen_bg">
      <video autoPlay muted loop playsInline class="fullscreen_bg_video">
        <source src="@/assets/bg-video.mp4" type="video/mp4" />
      </video>
    </div>

    <div class="brand"><img src="@/assets/logo.png" alt="Car selector"></div>
  </div>
</template>

<script>
export default {
  name: "FullScreenVideoBG",
};
</script>
<style scoped>
.brand {
  position: absolute;
  top: 0;
  text-transform: uppercase;
  font-size: 18px;
  font-weight: 600;
  margin: 35px 0 0 35px;
}
.brand img{
  height: auto;
  width: 75%;
}
.fullscreen_bg {
  position: fixed;
  top: 0;
  right: 0;
  width: 105%;
  height: 105%;
  overflow: hidden;
  z-index: -100;
}
.fullscreen_bg_video {
  height: 100%;
  min-width: 100%;
  object-fit: cover;
}

@media (max-width: 1100px) {
  .fullscreen_bg {
    min-width: 180%;
    height: 100%;
  }
}
</style>
