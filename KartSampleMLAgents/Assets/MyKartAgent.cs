using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Unity.MLAgents;
using Unity.MLAgents.Sensors;
using Unity.MLAgents.Actuators;

public class MyKartAgent : Agent
{
    public Transform sensors;
    public float speed = 1.0f;
    public float angularSpeed = 1.0f;
    float myHorizontal = 0; // front side
    Vector3 initialPosition;
    Quaternion initialRotation;

    // Start agent method
    public override void Initialize()
    {
        initialPosition = transform.position;
        initialRotation = transform.rotation;
    }

    // Actions to do when a training chapter begins
    public override void OnEpisodeBegin()
    {
        gameObject.transform.position = initialPosition;
        gameObject.transform.rotation = initialRotation;
        // begins with 0 velocity
        gameObject.GetComponent<Rigidbody>().velocity = Vector3.zero;
    }

    // Recolect observations and build the vector, to understand the enverioment 
    public override void CollectObservations(VectorSensor sensor)
    {
        // Pass trought each sensor of Paren Sensors game object
        for (int k = 0; k < sensors.childCount; k++)
        {
            // Get each vector
            Transform sensorK = sensors.transform.GetChild(k);
            RaycastHit hit;

            if (Physics.Raycast(sensorK.position, sensorK.forward, out hit, 100.0f))
                // if goes ok, register observations as objects, obstacles and their distance
                sensor.AddObservation(hit.distance);
            else
                // if for some reason is empty fill it anymway (shouldn't happen in this track)
                sensor.AddObservation(100.0f);
        }
    }

    // Execute actions (from keyboard, learn module or previuos module) automatically
    public override void OnActionReceived(ActionBuffers actionBuffers)
    {
        float action = angularSpeed * Mathf.Clamp(actionBuffers.ContinuousActions[0], -1.0f, 1.0f);
        myHorizontal = action;

        // while more time stay on the track it will get this reward (avoid crash to get it)
        SetReward(0.1f);
    }

    public override void Heuristic(in ActionBuffers actionsOut)
    {
        // build an action vector
        ActionSegment<float> continuousActionOut = actionsOut.ContinuousActions;
        continuousActionOut[0] = Input.GetAxis("Horizontal");
    }
}
