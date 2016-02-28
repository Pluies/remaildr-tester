var CurrentStatus = React.createClass({
  render: function() {
    var spanClass = "status-" + this.props.data.status;
    return (
<div className="col-md-12 center">
  <div className="topstatus">
    Current status:
    <span className={spanClass}>
      <strong> {this.props.data.status}</strong>
    </span>
  </div>
  <div>
    Last checked {this.props.data.last_checked}
  </div>
</div>
    );
  }
});
var StatusCircleList = React.createClass({
  render: function() {
    var statusCircleNodes = this.props.data.map(function(s) {
      var interval_title = "Last " + s.key
      return (
	<StatusCircle uptime={s.uptime}
                      uptime_int={s.uptime_int}
                      uptime_display={s.uptime_display}
                      interval={interval_title}
                      datapoints={s.datapoints}
                      key={s.key}/>
      );
    });
    return (
      <div className="statusCircleList">
        {statusCircleNodes}
      </div>
    );
  }
});

var StatusCircle = React.createClass({
  render: function() {
    return (
<div className="col-md-4 center">
  <h3>{this.props.interval}</h3>
  <div className="radial-progress" data-progress={this.props.uptime_int}>
    <div className="circle">
      <div className="mask full">
        <div className="fill"></div>
      </div>
      <div className="mask half">
        <div className="fill"></div>
        <div className="fill fix"></div>
      </div>
    </div>
    <div className="inset">
      <div className="percentage">
        <div className="numbers">
          <span>{this.props.uptime_display}</span>
        </div>
      </div>
    </div>
  </div>
  <span>Based on <span className="lightblue">{this.props.datapoints}</span> datapoints</span>
</div>
    );
  }
});

var StatusBox = React.createClass({
  loadStatusFromServer: function() {
    // Is it currently up?
    $.ajax({
      url: this.props.updown,
      dataType: 'json',
      cache: false,
      success: function(data) {
        this.setState({updown: data.updown});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.updown, status, err.toString());
      }.bind(this)
    });

    // Historical uptime data
    $.ajax({
      url: this.props.url,
      dataType: 'json',
      cache: false,
      success: function(data) {
        var arr = [];
	['day', 'month', 'year'].forEach(function(e, i, a){
          data.status[e].key = e;
          data.status[e].uptime_int = Math.round(data.status[e].uptime);
          data.status[e].uptime_display = +data.status[e].uptime.toFixed(2) + "%";
          arr.push(data.status[e]);
        });
        this.setState({data: arr});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },
  getInitialState: function() {
    return {data: [
      {key: 'day', datapoints: 0, uptime: 0, uptime_int: 0, uptime_display: ""},
      {key: 'month', datapoints: 0, uptime: 0, uptime_int: 0, uptime_display: ""},
      {key: 'year', datapoints: 0, uptime: 0, uptime_int: 0, uptime_display: ""}
    ],
    updown: {status: "down", last_checked: "never"}
    };
  },
  componentDidMount: function() {
    this.loadStatusFromServer();
    setInterval(this.loadStatusFromServer, this.props.pollInterval);
  },
  render: function() {
    return (
      <div>
        <div className="row">
          <CurrentStatus data={this.state.updown}/>
        </div>
        <div className="row">
          <StatusCircleList data={this.state.data} />
        </div>
      </div>
    );
  }
});

// Updates every 5mn
ReactDOM.render(
  <StatusBox url="/api/status" updown="/api/updown" pollInterval={5 * 60 * 1000} />,
  document.getElementById('content')
);
