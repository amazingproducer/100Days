// TODO: learn wtf is going on here

//import axios from 'axios'

window.longjacket = {
  // public key of the push notification server. 
  // if you are using the Test Push Notification Server, 
  // get public key from https://web-push-codelab.glitch.me/
  applicationServerPublicKey: 'BNAVJ63X40KbUEzSXqSW1C7Md9lcpj5TJF9Yk2_1hiaobNmk4Zx5HTcZ4wX-E4m_3gGdvUzz5MQROGDo8MiCr2Q',
  registration: null,
  isSubscribed: false,
  // render a button UI to subscribe/unsubscribe push notification
  // I am using Vue.js for the UI, though you can onvert it to use plain javascript or jQuery
  // TODO: Learn how this works and convert it to plain javascript
  initUi(options) {
    if ($('#lua-home-actionbar').length) {
      new Vue({
        el: '#lua-home-actionbar',
        data: {
          isSubscribed: options.isSubscribed
        },
        template: '<HomeActionBar :isSubscribedProp="isSubscribed" />',
        components: { HomeActionBar },
      })
    }
  },
  // call when service worker is registered
  checkSubscription(registration) {
    registration.pushManager.getSubscription()
      .then((subscription) => {
        this.isSubscribed = !(subscription === null)

        // send subscription info to server (the server will send push notification to this subscription)
        this.updateSubscriptionOnServer({ subscription: subscription, is_active: this.isSubscribed })

        this.registration = registration

        // update UI to indicate Push Notification is subscribed or not
        this.initUi({ isSubscribed: this.isSubscribed })
      })
  },
  // subscribe push notification
  subscribe() {
    const applicationServerKey = this.urlB64ToUint8Array(this.applicationServerPublicKey)

    return this.registration.pushManager.subscribe({
      // https://developers.google.com/web/fundamentals/push-notifications/subscribing-a-user#uservisibleonly_options
      // symbolic agreement with the browser that the web app will show 
      // a notification every time a push is received (i.e. no silent push).
      userVisibleOnly: true,
      applicationServerKey
    })
      .then((subscription) => {
        // subscription successful, send subscription info to server
        this.updateSubscriptionOnServer({ subscription, is_active: true })
        this.isSubscribed = true
        return true
      })
  },
  // unsubscribe push notification
  unsubscribe() {
    return this.registration.pushManager.getSubscription()
      .then((subscription) => {
        if (subscription) {
          // unsubscribe successful, update server
          this.updateSubscriptionOnServer({ subscription, is_active: false })
          this.isSubscribed = false
          return subscription.unsubscribe()
        }
        return false
      })
  },
  // send subscription info to server
  updateSubscriptionOnServer({ subscription, is_active }) {
    // if you are using https://web-push-codelab.glitch.me/ as a Test Push Notification Server
    // you need to copy and paste this string
    console.log(JSON.stringify(subscription))

    // if you implemented your own Push Notification Server
    
    axios({
      method: 'post',
      url: '/api/subscribe',
      data: {
        subscription_info: JSON.stringify(subscription),
        is_active: is_active
      }
    })
      .then((response) => {
        console.log(response.data)
      })
      .catch((error) => {
        console.log(error)
      })
      
  },
  // convert applicationServerPublicKey
  urlB64ToUint8Array(base64String) {
    const padding = '='.repeat((4 - base64String.length % 4) % 4)
    const base64 = (base64String + padding)
      .replace(/\-/g, '+')
      .replace(/_/g, '/')

    const rawData = window.atob(base64)
    const outputArray = new Uint8Array(rawData.length)

    for (let i = 0; i < rawData.length; ++i) {
      outputArray[i] = rawData.charCodeAt(i)
    }
    return outputArray
  }
}
