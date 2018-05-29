<template>
  <div class="row" id="login">
    <div class="col-xs-6 col-sm-6 col-md-4 col-lg-4 col-xs-offset-3 col-sm-offset-3 col-md-offset-4 col-lg-offset-4">
      <div class="header">
        <a v-bind:class="[way==='login'? 'active': '']" @click="changeWay('login')">&nbsp;&nbsp;&nbsp;&nbsp;登录&nbsp;&nbsp;&nbsp;&nbsp;·</a>
        <a v-bind:class="[way==='register'? 'active': '']" @click="changeWay('register')">&nbsp;&nbsp;&nbsp;&nbsp;注册&nbsp;&nbsp;&nbsp;&nbsp;</a>
      </div>
      <div class="alert alert-danger hide"></div>
      <div class="content">
        <form v-bind:class="['from-login', way==='login'? 'show': 'hide']">
          <div class="input-group usr">
            <span class="input-group-addon glyphicon glyphicon-user"></span>
            <input type="text" class="form-control" placeholder="Username" v-model="username">
          </div>
          <div class="input-group psd">
            <span class="input-group-addon glyphicon glyphicon-lock"></span>
            <input type="text" class="form-control" placeholder="Password" v-model="password">
          </div>
          <button class="btn btn-success btn-block" id="btn-submit" type="button" @click="login">登录</button>
        </form>
        <form v-bind:class="['from-register', way==='register'? 'show': 'hide']">
          <div class="input-group usr">
            <span class="input-group-addon glyphicon glyphicon-user"></span>
            <input type="text" class="form-control" placeholder="Username" v-model="usernameR">
          </div>
          <div class="input-group psd">
            <span class="input-group-addon glyphicon glyphicon-lock"></span>
            <input type="text" class="form-control" placeholder="Password" v-model="passwordR">
          </div>
          <button class="btn btn-success btn-block" id="btn-register" type="button" @click="register">注册</button>
        </form>
      </div>
    </div>
  </div>
</template>
<script>
export default {
    data: function() {
        return {
            username: '',
            password: '',
            usernameR: '',
            passwordR: '',
            way: 'login'
        }
    },
    methods: {
        login: function() {
            let self = this
            if(this.username && this.password) {
                this.$axios.post('/login', {usr: this.username, psd: this.password})
                .then(function(response) {
                    if(response.status === 200 && response.data.status === 'success') {
                      console.log(self)
                        self.$router.push('/')
                    }
                })
                .catch(function(error) {
                    console.log(error)
                })
            }
        },
        register: function() {
            console.log('register')
        },
        changeWay: function(way) {
            this.way = way;
        }
    }
}

</script>
<style>
    #login .show {
      display: block;
    }

    #login .hide {
      display: none;
    }

    #login {
      position: fixed;
      top: 0;
      bottom: 0;
      left: 0;
      right: 0;
      /*width: 100%;*/
      z-index: 1200;
      background-color: #f3f3f3;
      /*height: 100%;
      margin: 0;*/
      padding-top: 100px;
    }

    #login .row {
      margin-right: 0;
      margin-left: 0;
    }

    #login .glyphicon {
      top: 0;
    }

    #login .header {
      font-size: 17.5px;
    }

    #login .psd,
    #login button,
    #login form {
      margin-top: 20px;
    }

    #login a {
      color: #b1b1b1;
      text-decoration: none;
      cursor: pointer;
    }

    #login .active {
      color: #000;
    }
</style>
